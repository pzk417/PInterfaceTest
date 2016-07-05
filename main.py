# -*- coding: UTF-8 -*-

from appium import webdriver
from time import sleep
from unittest import TestCase

import desired_capabilities
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions

class MqcTest(TestCase):
    
    global ratioX, ratioY
    
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        self.driver = webdriver.Remote(uri, desired_caps)
        sleep(10);
        window_size  = self.driver.get_window_size();
	width = 720
	height = 1280
        self.ratioX = float("%.2f" % (float(window_size["width"]) / float(width)));
        self.ratioY = float("%.2f" % (float(window_size["height"]) / float(height)));
        
    def test_firstcase(self):
		sleep(1)
		self.click_element('com.cheyaoshi.merchant:id/input_account', '9', 386.0, 640.0, None)

		self.click_element('com.cheyaoshi.merchant:id/input_account', '请输入帐号', 501.0, 619.0, None)

		sleep(1)
		self.send_text('com.cheyaoshi.merchant:id/input_account', '请输入帐号', None, '95648')

		self.click_element('com.cheyaoshi.merchant:id/input_password', '', 405.0, 777.0, None)

		sleep(1)
		self.send_text('com.cheyaoshi.merchant:id/input_password', '', None, '666')

		sleep(2)
		self.click_element('com.cheyaoshi.merchant:id/read_checkbox', '', 107.0, 1035.0, None)

		sleep(2)
		self.click_element('com.cheyaoshi.merchant:id/login_btn', '登录', 299.0, 919.0, None)

		sleep(1)
		self.click_element('', '', 185.0, 322.0, None)

		sleep(2)
		self.click_element('com.cheyaoshi.merchant:id/month', '2016年06月', 183.0, 210.0, None)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/month_time', '04日07:14:43', 208.0, 208.0, None)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 50.0, 98.0, None)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 50.0, 98.0, None)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 50.0, 98.0, None)

		sleep(6)
		self.click_element('com.cheyaoshi.merchant:id/main_card_item_title', '财务结款', 514.0, 375.0, 1)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/money', '¥0.07', 384.0, 256.0, None)

		sleep(5)
		self.click_element('', '已结款金额:', 391.0, 375.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/payment_money_all', '¥0.01', 425.0, 377.0, None)

		sleep(7)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 34.0, 101.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/main_card_item_icon', '', 210.0, 688.0, 2)

		sleep(4)
		self.click_element('', '', 425.0, 313.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 34.0, 103.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 41.0, 89.0, None)

		sleep(4)
		self.click_element('', '', 514.0, 745.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/garage_qrcode', '', 370.0, 519.0, None)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 46.0, 103.0, None)

		sleep(3)
		self.click_element('', '', 46.0, 103.0, None)

		sleep(5)
		self.swipe([[352.0,949.0],[400.0,427.0],[401.0,428.0],[402.0,429.0]])

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/main_card_item_icon', '', 208.0, 882.0, 2)

		sleep(3)
		self.click_element('com.cheyaoshi.merchant:id/left_back_arrow', '', 48.0, 101.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/tab_icon', '', 549.0, 1211.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/logout', '退出登录', 434.0, 562.0, None)

		sleep(4)
		self.click_element('com.cheyaoshi.merchant:id/positiveButton', '确定', 251.0, 763.0, None)


        
    def tearDown(self):
        self.driver.quit()
    def swipe(self, points):
        automationName = self.driver.capabilities.get('automationName')
        last_x = 0
        last_y = 0
        if (automationName == 'Appium'):
            action_appium = TouchAction(self.driver)
            for i in range(0, len(points)):
                x = float(points[i][0]) * self.ratioX
                y = float(points[i][1]) * self.ratioY
                if (i == 0):
                    action_appium = action_appium.press(None, x, y).wait(200)
                elif (i == (len(points) - 1)):
                    action_appium = action_appium.move_to(None, x - last_x, y - last_y).wait(200).release()
                    action_appium.perform()
                else:
                    action_appium = action_appium.move_to(None, x - last_x, y - last_y).wait(200)
                last_x = x
                last_y = y
        else:
            action_selendroid = TouchActions(self.driver)
            for i in range(0, len(points)):
                x = float(points[i][0]) * self.ratioX
                y = float(points[i][1]) * self.ratioY
                if (i == 0):
                    action_selendroid.tap_and_hold(x, y)
                elif (i == (len(points) - 1)):
                    action_selendroid.move(x, y).release(x, y).perform()
                else:
                    action_selendroid.move(x, y)
    def id(self, resource_id):
        automationName = self.driver.capabilities.get('automationName')
        if (automationName == 'Appium'):
            return resource_id
        else:
            return resource_id.split('/')[1]
        
    def click_element(self, resource_id, desc, x, y, index):
        try:
            automationName = self.driver.capabilities.get('automationName')
            if (resource_id != ''):
                resource_id = self.id(resource_id)
                if (index == None):
                    self.driver.find_element_by_id(resource_id).click()
                else:
                    (self.driver.find_elements_by_id(resource_id)[index]).click()
            elif(desc != ''):
                if(automationName == 'Appium'):
                    self.driver.find_element_by_name(desc).click()
                else:
                    self.driver.find_element_by_link_text(desc).click()
            else:
                x = float(x) * self.ratioX
                y = float(y) * self.ratioY
                if(automationName == 'Appium'):
                    TouchAction(self.driver).press(None, x, y).release().perform()
                else:
                    TouchActions(self.driver).tap_and_hold(x, y).release(x, y).perform()
        except:
            try:
                self.driver.find_element_by_name(desc).click();
            except:
                raise Exception('未找到控件 resourceId: [' + resource_id + '] TEXT: [' + desc + ']')
        
    def tap(self, x, y):
        x = float(x) * float(self.ratioX)
        y = float(y) * float(self.ratioY)
        automationName = self.driver.capabilities.get('automationName')
        if (automationName == 'Appium'):
            return self.driver.tap([x, y], 500)
        else:
            return TouchAction(self.driver).press(None, x, y).release()
    def keycode(self, code, metastate):
        automationName = self.driver.capabilities.get('automationName')
        if (automationName == 'Appium'):
            return self.driver.press_keycode(code, metastate)
        else:
            return self.driver.keyevent(code, metastate)
    def send_text(self, resource_id, desc, index, text):
        try:
            if (resource_id != ''):
                resource_id = self.id(resource_id)
                if (index == None):
                    self.driver.find_element_by_id(resource_id).send_keys(text.decode('UTF-8'))
                else:
                    (self.driver.find_elements_by_id(resource_id)[index]).send_keys(text.decode('UTF-8'))
            elif(desc != ''):
                self.driver.find_element_by_name(desc).send_keys(text.decode('UTF-8'))
        except:
            raise Exception('未找到控件 resourceId: [' + resource_id + '] TEXT: [' + desc + ']')
