#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""
import pymysql.cursors


class WsproxyDb(object):

    def __init__(self, db_config, pid):
        self.sql = None
        self.data = dict()
        self.pid = pid
        self.db_config = db_config
        for key, value in self.db_config.items():
            setattr(self, key, value)
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db,
                                          charset=self.charset,
                                          cursorclass=pymysql.cursors.DictCursor
                                          )

    def log_url(self, request):
        self.data['pid'] = self.pid
        self.data['method'] = request.method
        self.data['url'] = request.url
        self.data['raw'] = request.raw_content
        with self.connection.cursor() as cursor:
            self.sql = "insert into ws_url(pid, method, url, raw) values (%s,%s,%s,%s)"
            cursor.execute(self.sql, (self.data['pid'], self.data['method'], self.data['url'], self.data['raw']))
        self.connection.commit()
        cursor.close()
