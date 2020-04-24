import pytest
import allure
from Page.init_page import InitPage


class TestHome:
    def setup_class(self):
        self.driver = InitPage()
        self.home = self.driver.goto_home()

    @allure.description("切换房间")
    def test_room_change(self):
        for i in range(3):
            self.home.change_room()
        self.home.allure_screenshot(story="截图")