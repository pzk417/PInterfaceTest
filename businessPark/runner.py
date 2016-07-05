#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import unittest
import xlrd
import json
import time
import ConfigParser

from basehttp import BaseHttp
from confighttp import ConfigHttp
from htmlreport import HtmlReport

# 读取并配置接口服务器IP，端口等信息
base_http = BaseHttp('d:\\conf.ini')

# 定义结构体
class DataStruct:
    '''于接收excel读取的测试数据,记录要写入测试报告的数据'''
    pass

test_data = DataStruct()
test_data.url = ''               # 接收接口url
test_data.params = {}            # 接收接口参数
test_data.expected_result = {}   # 接收预期结果
test_data.result = 'Fail'       # 接收测试结果

# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
   def setUp(self):
       self.config_http = ConfigHttp(base_http.get_host(), base_http.get_port())

   # 测试接口1
   def test_get_diffcheckcode(self):
       # 根据被测接口的实际情况，合理的添加HTTP头
       header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'
          }
       self.config_http.set_header(header)

       response = self.config_http.get(test_data.url, test_data.params)
       if {} == response:
           test_data.result = 'Error'
           html_report.error_num = html_report.error_num + 1
           return
       try:
           self.assertEqual(response['msg'], test_data.expected_result, msg='exception')
           test_data.result = 'Pass'
           html_report.success_num = html_report.success_num + 1
       except AssertionError:
           test_data.result = 'Fail'
           html_report.fail_num = html_report.fail_num + 1

   # 测试接口2
   def test_get_checkcode(self):
       header = {'Content-Type':'application/json','charset':'utf-8'}
       self.config_http.set_header(header)
       response = self.config_http.post(test_data.url, test_data.params)
       if {} == response:
           test_data.result = 'Error'
           html_report.error_num = html_report.error_num + 1
           return
       try:
           self.assertEqual(response['msg'], test_data.expected_result, msg='exception')
           print(response['msg'])
           test_data.result = 'Pass'
           html_report.success_num = html_report.success_num + 1
       except AssertionError:
           test_data.result = 'Fail'
           html_report.fail_num = html_report.fail_num + 1

   def tearDown(self):
       pass

# 获取测试套件
def get_test_suite(index):
    test_suite = unittest.TestSuite()
    function = sheet1.row_values(index)[8] # 根据选择的用例，获取对应的测试用例方法
    test_suite.addTest(TestInterfaceCase(function))
    return test_suite

# 运行测试用例函数
def run_case(sheet, runner, config_file=''):
    html_report.case_total = 0
    config = ConfigParser.ConfigParser()

    # 从配置文件中读取要运行测试的测试用例所在行索引
    config.read(config_file)
    try:
        run_mode = config.get('DEFAULT','runmode')
        run_mode = int(run_mode)  # 把字符串类型的转换为list
        html_report.run_mode = run_mode
    except Exception:
        print('error happend in case config_file')

    if True == run_mode:  # 运行全部用例
        # 获取用例个数
        test_case_num = sheet.nrows

        # 循环执行测试用例
        for index in range(1, test_case_num):
            test_data.url = sheet.row_values(index)[4]
            test_data.params = json.loads(sheet.row_values(index)[5])
            test_data.expected_result = sheet.row_values(index)[6]
            test_suite = get_test_suite(index)
            runner.run(test_suite)

            # 记录运行结果
            sheet1.put_cell(index, 7, 1, test_data.result, 0)

            # 测试用例数加1
            html_report.case_total = html_report.case_total + 1

    else:   # 运行部分用例
        try:
            case_list = config.get('DEFAULT','index')
            case_list = eval(case_list)  # 把字符串类型的list转换为list
            html_report.case_list = case_list
        except Exception:
            print('error happend in case config_file')

         # 循环执行测试用例
        for index in case_list:
            test_data.url = sheet.row_values(index)[4]
            test_data.params = json.loads(sheet.row_values(index)[5])
            test_data.expected_result = sheet.row_values(index)[6]
            test_suite = get_test_suite(index)
            runner.run(test_suite)

            # 记录运行结果
            sheet1.put_cell(index, 7, 1, test_data.result, 0)

            # 测试用例数加1
            html_report.case_total = html_report.case_total + 1

# 运行测试套件
if __name__ == '__main__':
    # 记录测试开始时间
    start_time = time.time()

    runner = unittest.TextTestRunner()
    html_report = HtmlReport()

    # # 读取用例数据
    excel = xlrd.open_workbook('TestCase.xlsx')
    sheet1 = excel.sheet_by_index(0)

    run_case(sheet1, runner, 'run.conf')

    # 测试结束时间
    end_time = time.time()
    html_report.time_caculate(end_time - start_time)  # 计算测试消耗时间

    # 生成测试报告
    html_report.generate_html('test report', sheet1, 'report.html')