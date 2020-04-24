import os
from time import sleep
from selenium.webdriver.common.by import By
from Common.base import BasePage
import yaml

base_path = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(base_path, "..", "config.yaml"))
with open(p, 'r')as f:
    data = yaml.safe_load(f)
# 本地化配置文件时使用
# phone = data["Phone"]
# Jenkins服务参数化时使用
phone = os.environ["phone"]
phone_path = os.path.abspath(os.path.join(base_path, "..", "Image", phone))


class HomePage(BasePage):
    _always = (By.XPATH, '//android.widget.TextView[@text="常用设备"]')
    _living = (By.XPATH, '//android.widget.TextView[@text="客厅"]')

    def change_room(self):
        self.find_element_until_visibility(self._living).click()
        sleep(2)
        self.save_screen_shot(phone_path, "01.png")
        self.find_element_until_visibility(self._always).click()
        sleep(2)
        self.save_screen_shot(phone_path, "02.png")
        return self