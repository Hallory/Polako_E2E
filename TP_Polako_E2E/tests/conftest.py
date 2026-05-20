import os
import re
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

ROOT_DIR = Path(__file__).resolve().parent.parent


load_dotenv(ROOT_DIR / ".env")

ENVIRONMENTS = {
    "stg": os.getenv("STG_URL"),
    "prod": os.getenv("PROD_URL"),
}

missing = [name for name, value in ENVIRONMENTS.items() if not value]

if missing:
    raise RuntimeError(f"Missing env variables: {', '.join(missing)}")


ARTIFACTS_DIR = ROOT_DIR / "artifacts"

SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
VIDEOS_DIR = ARTIFACTS_DIR / "videos"
TRACES_DIR = ARTIFACTS_DIR / "traces"

for directory in (
    SCREENSHOTS_DIR,
    VIDEOS_DIR,
    TRACES_DIR,
):
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="stg",
        help="Environment: stg/prod",
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "smoke: smoke tests",
    )

    config.addinivalue_line(
        "markers",
        "regression: regression tests",
    )

    config.addinivalue_line(
        "markers",
        "ui: ui tests",
    )


@pytest.fixture(scope="session")
def base_url(pytestconfig):

    env = pytestconfig.getoption("--env")

    if env not in ENVIRONMENTS:
        raise ValueError(f"Unknown environment: {env}")

    return ENVIRONMENTS[env]


@pytest.fixture(scope="session")
def browser_type_launch_args(
    browser_type_launch_args,
):

    return {
        **browser_type_launch_args,
        "headless": os.getenv(
            "HEADLESS",
            "false",
        ).lower()
        == "true",  # true
    }


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args,
):

    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_dir": str(VIDEOS_DIR),
    }


@pytest.fixture
def app_page(
    page: Page,
    base_url,
    request,
):
    test_name = request.node.name

    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page.set_default_timeout(10_000)
    page.set_default_navigation_timeout(30_000)

    page.context.clear_cookies()

    page.goto(
        base_url,
        wait_until="domcontentloaded",
    )

    page.evaluate(
        "() => {" "window.localStorage.clear();" "window.sessionStorage.clear();" "}"
    )

    page.reload()

    try:
        yield page

    finally:
        safe_name = re.sub(
            r'[<>:"/\\\\|?*]',
            "_",
            test_name,
        )

        trace_path = TRACES_DIR / f"{safe_name}.zip"

        page.context.tracing.stop(path=str(trace_path))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call,
):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.passed:
        return

    page = item.funcargs.get("app_page") or item.funcargs.get("page")

    if not page:
        return

    safe_name = re.sub(
        r'[<>:"/\\\\|?*]',
        "_",
        item.name,
    )

    screenshot_path = SCREENSHOTS_DIR / f"{safe_name}.png"

    page.screenshot(
        path=str(screenshot_path),
        full_page=True,
    )
