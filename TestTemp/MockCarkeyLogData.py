# -*- coding:utf-8 -*-
"""
 测试车辆进出报表 造数据
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
t_yunpark_event_elapsed_time
EntryElapsedTime
 1 - 其他入库
 2 - 识别入库
 3 - 扫码入库
 ExitElapsedTime
 1 - 全部出库
 2 - 识别出库
 3 - 扫码出库
 PayElapsedTime
 1 - 扫码支付
 智慧园车库 1个月 每天造300条进出记录 提供做聚合
'''
def insertt_yunpark_elapsed_time(group_date,garage_guid):
    minsertsql="INSERT INTO public.t_yunpark_event_elapsed_time " \
              "(guid, order_guid, garage_guid, group_date, elapsed_type, group_type, group_value, create_time, update_time, is_delete) " \
               "VALUES('%s', '%s', '%s', '%s', '%s',  %d, '%s', '%s', '%s', false)"
    #订单
    order_guid=str(uuid.uuid4()).replace('-','')
    gtypedict = {'EntryElapsedTime':3,'ExitElapsedTime':3,'PayElapsedTime':1}
    try:
        for (k,v) in gtypedict.items():
            t_uuid = str(uuid.uuid4()).replace('-','')
            create_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            update_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            elapsed_type = str(k)
            rgroup_type = random.sample(range(1,v+1),1)
            group_type = rgroup_type[0]
            group_value = round(random.randint(77,77777)/1000.00,3)
            insertsql= minsertsql%(t_uuid,order_guid,garage_guid,group_date,elapsed_type,group_type,group_value,create_time,update_time)
            cur.execute(insertsql)
    except Exception, e:
        print e.message
    #每次执行完 就commit一次
    conn.commit()


if __name__ == '__main__':
    # 8209cdb9ce2f4572a46415fce9da2324 智慧园停车场
    for i in xrange(0,30):
        daytime = date.today() + timedelta(days = -i)
        print daytime
        for n in xrange(0,300):
            insertt_yunpark_elapsed_time(str(daytime),'8209cdb9ce2f4572a46415fce9da2324')
    cur.close()
    conn.close()













