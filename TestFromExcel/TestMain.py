#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'pzk'

import unittest
import xlrd
import json
import time
import configparser


if __name__ == '__main__':

     with xlrd.open_workbook('../TestCase.xlsx') as f:
          sheet1 = f.sheet_by_index(0)
          print sheet1.name
          test_case_num = sheet1.nrows
          for index in range(1, test_case_num):
              print sheet1.row_values(index)[4]

     # #读取case文件
     # excel = xlrd.open_workbook('../TestCase.xlsx')
     # #读取第一个excel
     # sheet1 = excel.sheet_by_index(0)
     # #得到case组名称
     # print sheet1.name
     # #按照行读取
     # test_case_num = sheet1.nrows
     # # 循环执行测试用例
     # for index in range(1, test_case_num):
     #     print sheet1.row_values(index)[4]