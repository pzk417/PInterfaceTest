#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import urllib.request
import urllib.parse
import json

# 配置类
class ConfigHttp:
    '''用于封装http请求方法，http头设置'''

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.headers = {}  # http 头

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装HTTP GET请求方法
    def get(self, url, params):
        params = urllib.parse.urlencode(params)  # 将参数转为url编码字符串
        url = 'http://' + self.host + ':' + str(self.port)  + url + params
        request = urllib.request.Request(url, headers=self.headers)
        try:
            response = urllib.request.urlopen(request)
            response = response.read().decode('utf-8')  # decode函数对获取的字节数据进行解码
            json_response = json.loads(response)  # 将返回数据转为json格式的数据
            return json_response
        except Exception:
            print('no json data returned')
            return {}

    # 封装HTTP POST请求方法
    def post(self, url, data):
        #data = urllib.parse.urlencode(data)
        #data = data.encode('utf-8')
        data = json.dumps(data)
        data = data.encode('utf-8')
        url = 'http://' + self.host + ':' + str(self.port)  + url
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request, data)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            print(json_response)
            return json_response
        except Exception:
            print('no json data returned')
            return {}

    # 封装HTTP xxx请求方法
    # 自由扩展