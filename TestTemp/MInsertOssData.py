# -*- coding:utf-8 -*-
"""
 测试车辆进出报表，模拟用户支付

"""

__author__ = 'pzk'

import psycopg2
import psycopg2.extras
import json
import uuid
import time
from datetime import timedelta, date
import random

pgurl=r'jdbc:postgresql://120.55.116.53:3434/db_carkey_log'
host='120.55.116.53'
pgname='db_carkey_log'
pguser='_carkey'
pgport=3434
pgpwd='_carkey'
conn=psycopg2.connect(database=pgname,user=pguser,password=pgpwd,host=host,port=pgport)
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

'''
INSERT INTO public.t_yunpark_elapsed_time
(guid, group_date, garage_guid, all_entry_elapsed_time, identify_entry_elapsed_time, scan_entry_elapsed_time, all_exit_elapsed_time, identify_exit_elapsed_time, scan_exit_elapsed_time, scan_pay_elapsed_time, create_time, update_time, is_delete)
VALUES('', '', '', 0, 0, 0, 0, 0, 0, 0, '', '', false);
8209cdb9ce2f4572a46415fce9da2324
all_entry_elapsed_time:保留字段
identify_entry_elapsed_time:入库耗时(车牌识别)
scan_entry_elapsed_time 入库耗时(扫码识别)
all_exit_elapsed_time:保留字段
identify_exit_elapsed_time 出库耗时(车牌识别)
scan_exit_elapsed_time 出库耗时(扫码识别)
scan_pay_elapsed_time 扫码支付耗时
'''
def insertt_yunpark_elapsed_time(uuidstr,group_date,garage_guid):
    minsertsql="INSERT INTO public.t_yunpark_elapsed_time " \
              "(guid, group_date, garage_guid, all_entry_elapsed_time, identify_entry_elapsed_time, scan_entry_elapsed_time, all_exit_elapsed_time, identify_exit_elapsed_time, scan_exit_elapsed_time, scan_pay_elapsed_time, create_time, update_time, is_delete) VALUES('%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, '%s', '%s', false)"
              # "VALUES('%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, '%s', '%s', false)“
    createtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    all_entry_elapsed_time = random.randint(100,1000)
    identify_entry_elapsed_time= random.randint(30,1000)
    scan_entry_elapsed_time = random.randint(100,1000)
    all_exit_elapsed_time= random.randint(50,1000)
    identify_exit_elapsed_= random.randint(100,1000)
    scan_exit_elapsed_time = random.randint(100,1000)
    scan_pay_elapsed_time = random.randint(200,1000)
    insertsql= minsertsql%(uuidstr,group_date,garage_guid,all_entry_elapsed_time,identify_entry_elapsed_time,scan_entry_elapsed_time,all_exit_elapsed_time,identify_exit_elapsed_,scan_exit_elapsed_time,scan_pay_elapsed_time,createtime,updatetime)
    print insertsql
    try:
        cur.execute(insertsql)
    except Exception, e:
        print 'insert record into table failed'


if __name__ == '__main__':
    # 8209cdb9ce2f4572a46415fce9da2324 智慧园停车场
    for i in xrange(0,30):
        uuidstr = str(uuid.uuid4()).replace('-','')
        daytime = date.today() + timedelta(days = -i)
        print uuidstr
        print daytime
        # insertt_yunpark_elapsed_time(uuidstr,str(daytime),'8209cdb9ce2f4572a46415fce9da2324')

    conn.commit()
    cur.close()
    conn.close()













