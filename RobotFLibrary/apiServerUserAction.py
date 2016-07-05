# -*- coding:utf-8 -*-

import base64,sys

__author__ = 'pzk'

class RC4Utils():
    '''Base64
    '''
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

    def encryptFromBase64(self,key,str):
        source = base64.b64encode(str)
        docryptStr = self.docrypt(key, source)
        result = base64.b64encode(docryptStr)
        return result

    def docrypt(self,key,string):
        string_lenth = len(string)
        result = ''
        box = list(range(256))
        j = 0
        x = 0

        for i in xrange(0,256):
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



