#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'pzk'

import unittest
import xlrd
import json
import time
import configparser


if __name__ == '__main__':
     excel = xlrd.open_workbook('../TestCase.xlsx')
     sheet1 = excel.sheet_by_index(0)
     print sheet1
     test_case_num = sheet1.nrows
     # 循环执行测试用例
     for index in range(1, test_case_num):
         print sheet1.row_values(index)[4]

