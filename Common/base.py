import logging
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import allure


class BasePage:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  -  %(message)s')

    logger = logging.getLogger(__name__)

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element_until_visibility(self, locator, timeout=10) -> WebElement:
        """
        隐式等待方式查找单个控件元素
        :param locator: 控件元素的属性
        :param timeout: 超时时间,默认10s
        :return: 返回控件元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    def find_elements_until_visibility(self, locator, timeout=10) -> WebElement:
        """
        隐式等待方式查找多个控件元素
        :param locator: 控件元素的属性
        :param timeout: 超时时间,默认10s
        :return: 返回控件元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    def is_element(self, locator, timeout=10):
        """
        判断当前页面是否包含某元素
        :param locator: 控件元素的属性
        :param timeout: 超时时间,默认10s
        :return: 返回True or False
        """
        Flag = None
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            Flag = True
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
            Flag = False
        finally:
            return Flag

    def swipe(self, start_x, start_y, end_x, end_y, dur=800):
        """
        滑动操作
        :param start_x: 起始横坐标
        :param start_y: 起始纵坐标
        :param end_x: 终点横坐标
        :param end_y: 终点纵坐标
        :param dur: 在多长时间内完成滑动操作(单位:ms)
        """
        return self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=dur)

    def is_element_and_swipe(self, locator, timeout=10):
        """
        判断当前页面是否有指定元素,没有则下滑
        """
        while 1:
            flag = self.is_element(locator, timeout)
            if flag:
                break
            else:
                self.driver.swipe(300, 800, 300, 0, 1000)
                sleep(1)
        return self

    def swipe_ele_left(self, ele, dur=800):
        """
        基于控件元素左滑操作
        :param ele: 控件元素
        :param dur: 滑动时间
        """
        start_x = int(ele.rect["width"]) - 20
        end_x = int(ele.rect["x"])
        height = int(ele.rect["y"]) + int(ele.rect["height"]) / 2
        # self.driver.swipe
        self.swipe(start_x, height, end_x, height, dur)
        sleep(1)
        return self

    def toast_locator(cls):
        """
        用于Toast检验
        :return:
        """
        return (By.XPATH, "//*[@class='android.widget.Toast']")

    def allure_screenshot(self, title="测试截图", story="Nomal"):
        """
        allure报告截图
        :param title: 截图title
        :param story:
        :return:
        """
        with allure.step(title):
            allure.attach(self.driver.get_screenshot_as_png(), story, allure.attachment_type.PNG)
        return self

    def save_screen_shot(self, path, file):
        """
        将截屏保存到本地,兼容性测试可用于检查各页面截图
        :param path: 图片保存目录
        :param file: 文件名称
        :return:
        """
        filename = os.path.abspath(os.path.join(path, file))
        self.driver.get_screenshot_as_file(filename)


