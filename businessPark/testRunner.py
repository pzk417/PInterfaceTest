# -*- coding:utf-8 -*-
__author__ = 'pzk'

import json
import time
import unittest
import xlrd
from common.htmlreport import HtmlReport
import ConfigParser
import urllib


# 定义结构体
class DataStruct:
    '''于接收excel读取的测试数据,记录要写入测试报告的数据'''
    pass

test_data = DataStruct()
test_data.url = ''               # 接收接口url
test_data.params = {}            # 接收接口参数
test_data.expected_result = {}   # 接收预期结果
test_data.result = 'Fail'        # 接收测试结果

html_report = HtmlReport()

# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
   def setUp(self):
       self.serverurl = ''

   # 测试get类型接口
   def test_get(self):
       data = json.dumps(test_data.params)
       data = data.encode('utf-8')
       header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'
          }
       try:
           request = urllib.request.Request(self.serverurl, headers=header)
           response = urllib.request.urlopen(request)
           response = response.read().decode('utf-8')
           json_response = json.loads(response)
           print "返回的结果为%s"%(json_response)
           try:
               self.assertEqual(json_response['msg'], test_data.expected_result, msg='exception')
               print(json_response['msg'])
               test_data.result = 'Pass'
               html_report.success_num = html_report.success_num + 1
           except AssertionError:
               test_data.result = 'Fail'
               html_report.fail_num = html_report.fail_num + 1
       except Exception:
           print('no json data returned')
           return {}

   # 测试post类型接口
   def test_post(self):
       data = json.dumps(test_data.params)
       data = data.encode('utf-8')
       header = {'Content-Type':'application/json','charset':'utf-8'}
       try:
           request = urllib.request.Request(self.serverurl, headers=header)
           response = urllib.request.urlopen(request, data)
           response = response.read().decode('utf-8')
           json_response = json.loads(response)
           print "返回的结果为%s"%(json_response)
           try:
               self.assertEqual(json_response['msg'], test_data.expected_result, msg='exception')
               print(json_response['msg'])
               test_data.result = 'Pass'
               html_report.success_num = html_report.success_num + 1
           except AssertionError:
               test_data.result = 'Fail'
               html_report.fail_num = html_report.fail_num + 1
       except Exception:
           print('no json data returned')
           return {}

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
        run_mode = config.get("TestModel","runmode")
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
            case_list = config['DEFAULT']['index']
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
