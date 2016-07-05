# -*- coding:utf-8 -*-

from common import RedisUtil
import unittest,json,time

# 定义结构体
class DataStruct:
    '''于接收excel读取的测试数据,记录要写入测试报告的数据'''
    pass

test_data = DataStruct()
test_data.url = ''               # 接收接口url
test_data.params = {}            # 接收接口参数
test_data.expected_result = {}   # 接收预期结果
test_data.result = 'Fail'        # 接收测试结果


class DriverInterfaceCase(unittest.TestCase):

    #测试环境的初始化
    def setUp(self):
        self.url = ''
        self.redisurl=''
        self.dburl=''

    #停车员登录
    def testDriverLogin(self):
        inputparam = json.loads(test_data.params)
        driverMobile = inputparam['driverMobile']
        token = RedisUtil.getValueForKey(driverMobile)

        pass

    def testDriverPushOrder(self):
        pass

    def testUpdatePostion(self):
        pass

    def testDoOrder(self):
        pass

    #测试环境的销毁
    def tearDown(self):
        pass










