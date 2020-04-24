import pytest
import allure
from Page.init_page import InitPage

class TestMine:
    def setup_class(self):
        self.driver = InitPage()
        self.mine = self.driver.goto_mine()

    @allure.description("切换房间")
    def test_room_change(self):
        # for i in range(3):
        self.mine.into_info()
        self.mine.allure_screenshot(story="截图")

    @allure.description("比较两值是否相等")
    def test_add(self):
        a = 2
        b = 3
        c = a+b
        d = a*b
        assert c==d,"计算有误"