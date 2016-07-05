# coding:utf8
"""
Created on 15/12/10
 
@author: mengchuang
"""

import json
import urllib2
import sys
import base64
import thread

reload(sys)
sys.setdefaultencoding('utf-8')


def encryptFromBase64(key, str):
    source = base64.b64encode(str)
    decryptStr = decrypt(key, source)
    result = base64.b64encode(decryptStr)
    return result


def decrypt(key, string):
    string_lenth = len(string)
    result = ''
    box = list(range(256))
    j = 0
    x = 0

    for i in xrange(0, 256):
        box[i] = i

    for i in xrange(256):
        j = (j + box[i] + (ord(key[i % len(key)]))) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp

    i = 0
    j = 0
    for y in xrange(string_lenth):
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp
        result += unichr((ord(string[y])) ^ (box[(box[i] + box[j]) % 256]))
    return result


def do_post(url, params):
    data = json.dumps(params)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    result = json.loads(response.read())
    return result


url = 'http://uat.cheyaoshi.com/api'

token = 'ee3efd017e335dc7c74656172f7fc64e'
key = 'iEOdXDs817LCsi/uzy6TqQ=='

accept_params = dict()
accept_params['action'] = 'user.take.request'

data1 = encryptFromBase64(key, json.dumps(accept_params))

data2 = encryptFromBase64(key, json.dumps(accept_params))


def a():
    print ("a")
    params = dict()
    params['data'] = data1
    params['token'] = token
    result = do_post(url, params)
    print result


def b():
    print ("b")
    params = dict()
    params['data'] = data2
    params['token'] = token
    result = do_post(url, params)
    print result


thread.start_new_thread(a, ())
b()
import time
time.sleep(5)