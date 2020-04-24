import os
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from Common.base import BasePage
from Page.home_page import HomePage
from Page.mine_page import MinePage
from Page.scene_page import ScenePage


class InitPage(BasePage):
    # driver = None
    _mine = (By.XPATH, '//android.widget.TextView[@text="我的"]')
    _scene = (By.XPATH, '//android.widget.TextView[@text="场景"]')
    _home = (By.XPATH, '//android.widget.TextView[@text="首页"]')
    driver: webdriver = None
    desired_caps = {}
    base_path = os.path.dirname(__file__)
    p = os.path.abspath(os.path.join(base_path, "..", "config.yaml"))
    with open(p, 'r')as f:
        data = yaml.safe_load(f)
    platformName = data["platformName"]
    appPackage = data["appPackage"]
    appActivity = data["appActivity"]
    desired_caps["platformName"] = data["platformName"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = True
    desired_caps["deviceName"] = "Mi"
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True

    # 新增Port参数,Jenkins服务参数化时使用
    port = os.environ["port"]

    def first_start(self):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        # Jenkins服务参数化时使用
        self.driver = webdriver.Remote('http://localhost:{port}/wd/hub'.format(port=self.port), self.desired_caps)
        self.driver.implicitly_wait(20)
        InitPage.driver = self.driver

    def __init__(self):
        if InitPage.driver == None:
            self.first_start()
        else:
            pass

    def goto_mine(self):
        self.find_element_until_visibility(self._mine).click()
        return MinePage(self.driver)

    def goto_scene(self):
        self.find_element_until_visibility(self._scene).click()
        return ScenePage(self.driver)

    def goto_home(self):
        self.find_element_until_visibility(self._home).click()
        return HomePage(self.driver)
