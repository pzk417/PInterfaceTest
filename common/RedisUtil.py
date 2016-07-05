# -*- coding:utf-8 -*-
'''
 redis 工具类
'''
__author__ = 'pzk'

import redis

host = '120.26.63.129'
pwd = 'ckRedis@!'

redisSer = redis.StrictRedis(host=host, password=pwd,port=6379,db=0)

class RedisUtil:

    def __int__(self):
        pass

    def getValueForKey(self,key):
        if key:
            return redisSer.get(key)
        else:
            return 'nokey'

    def setKeyValue(self,key,value):
        if key and value:
            redisSer.set(key,value)


    def delKey(self,key):
        if key:
            redisSer.delete(key)










