import os
from time import sleep
import yaml
from selenium.webdriver.common.by import By
from Common.base import BasePage

base_path = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(base_path, "..", "config.yaml"))
with open(p, 'r')as f:
    data = yaml.safe_load(f)
# 本地化配置文件时使用
# phone = data["Phone"]
# # Jenkins服务参数化时使用
phone = os.environ["phone"]
phone_path = os.path.abspath(os.path.join(base_path, "..", "Image", phone))




class MinePage(BasePage):
    _name = (By.XPATH, '//android.widget.TextView[@text="4套房屋"]')
    _back = (By.XPATH, '//android.widget.TextView[@text=""]')

    def into_info(self):
        self.find_element_until_visibility(self._name).click()
        sleep(2)
        self.save_screen_shot(phone_path, "03.png")
        self.find_element_until_visibility(self._back).click()
        sleep(2)
        self.save_screen_shot(phone_path, "04.png")
        return self