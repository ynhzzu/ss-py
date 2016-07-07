#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tailer
import re
import redis

#logs = tailer.tail(open('/var/log/shadowsocks.log'), 10)
logs = tailer.follow(open('/var/log/shadowsocks.log'))
pattern = re.compile(r'([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2}) INFO     host:([^ ]+) port:([0-9]+) connecting ([^ ]+) from ([^ ]+) ip:([^ ]+)')
for line in logs:
    match = pattern.match(line)
    r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, password = 'root123')
    if match:
        date = match.group(1)
        if date.split('-')[2] == '01':
            r.flushdb()
        port = match.group(4)
        ip = match.group(7)
        r.hincrby('ss:' + port, ip, 1)
        print date + '\t' + port + '\t' + ip
