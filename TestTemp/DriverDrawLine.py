# -*- coding:utf-8 -*-
"""
从数据库里面读取服务区的经纬度，让停车员按照此经纬度更新位置
"""

__author__ = 'pzk'

import psycopg2
import psycopg2.extras
import json

pgurl=r'jdbc:postgresql://120.26.63.129:8932/carkeyv2'
host='120.26.63.129'
pgname='carkeyv2'
pguser='_carkey'
pgport=8932
pgpwd='carkey123'
drivermoblie='18000000001'
conn=psycopg2.connect(database=pgname,user=pguser,password=pgpwd,host=host,port=pgport)
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def drawLineFromFile(driverphone,pathfile):
    driversql="select guid from t_driver where mobile_phone='%s'"%driverphone
    cur.execute(driversql)
    sguid =  cur.fetchone()['guid']
    with open(pathfile) as f:
        for ll in f.readlines():
            datestr = ll[:ll.index('{')]
            lnglat = json.loads(ll[ll.index('{'):])
            lng =lnglat['lng']
            lat =lnglat['lat']
            postionsql ="update t_driver_position set lat=%s ,lng=%s where driver_guid='%s'"%(lat,lng,sguid)
            print postionsql
            cur.execute(postionsql)

if __name__ == '__main__':
    driverphone = "18516633905"
    filepath = "/Users/pzk/Downloads/gulei.txt"
    drawLineFromFile(driverphone,filepath)

    garagesql="select coverage_range from public.t_service_area_coverage_range where service_area_guid='df14e7b356d54ee0a6119ac1fb5958e3'"
    cur.execute(garagesql)
    sratlng =  cur.fetchone()
    driversql="select guid from t_driver where mobile_phone='%s'"%drivermoblie
    cur.execute(driversql)
    sguid =  cur.fetchone()['guid']

    print sguid
    #print sratlng
    latlng =  sratlng['coverage_range'][9:][:-2]
    print latlng
    print latlng.split(',')
    for ll in latlng.split(','):
        lat = ll.split(' ')[1]
        lng = ll.split(' ')[0]
        postionsql ="update t_driver_position set lat=%s ,lng=%s where driver_guid='%s'"%(lat,lng,sguid)
        print postionsql
        cur.execute(postionsql)
    conn.commit()
    cur.close()
    conn.close()












