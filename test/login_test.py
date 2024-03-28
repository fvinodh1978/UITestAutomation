import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from webdriver_manager.core.driver_cache import DriverCacheManager
from webdriver_manager.core.os_manager import OperationSystemManager
from webdriver_manager.firefox import GeckoDriverManager

# this test class covers all the scenarios related to authentication
class TestLogin:
    # @pytest.mark.ignore
    def test_title(self):
        expected_title="Automation Remarks"
        driver = webdriver.Firefox()
        driver.get("http://automation-remarks.com")
        actual_title=driver.title

        assert driver.title == expected_title
        driver.quit()
