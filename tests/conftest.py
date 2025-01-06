import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.config import Resources

@pytest.fixture(scope="function")
def setup(request):
    global driver
    options = Options()
    options.add_argument("--start-maximized")

    # Specify the path to the downloaded ChromeDriver
    service = Service(Resources.WINDOWS_CHROME_DRIVER)
    try:
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        raise Exception(f"WebDriver initialization failed: {str(e)}")

    # Attach driver instance to the test class
    request.cls.driver = driver
    driver.get(os.environ.get('Dashboard', Resources.BASE_URL))

    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = (Resources.SCREENSHOTS_DIR + report.nodeid.replace("::", "_") + ".png").replace("tests/", "")
            print(file_name)
            #_capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)


def pytest_html_report_title(report):
    report.title = "CDE Automation Testing Report"

