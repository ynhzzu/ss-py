#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, password = 'root123')
keys = r.keys('ss:*')
for key in keys:
    dic = {}
    for hkey in r.hkeys(key):
        dic[hkey] = int(r.hget(key, hkey))
    sort_dic = sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
    st = ''
    for k,v in sort_dic:
        st = st + '(' + k + ', ' + str(v) + '),'
    st = st[0 : -1]
    print key + '\t' + st

