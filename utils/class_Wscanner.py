#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

import os
from utils.WsproxyDb import *
from utils.class_Sqlmap import SqlmapApi


class Wscanner(object):
    def __init__(self, db_config, pid):
        self.pid = pid
        self.db_config = db_config
        self.wsdb = WsproxyDb(self.db_config, self.pid)
        self.sqlmap_api = SqlmapApi()

    def run(self):
        raw = self.wsdb.get_url(0)
        url_file = self.get_url_file(raw)
        if self.sqlmap_api.start(url_file):
            print "%s 存在sql注入" % url_file
        else:
            print "%s 不存在sql注入" % url_file

    @staticmethod
    def get_url_file(raw):
        url_file = os.getcwd() + '/tmp/url_' + str(raw['id']) + '.txt'
        with open(url_file, 'w') as f:
            f.write(raw['method'] + ' ' + raw['url'] + ' HTTP/1.1' + '\n')
            f.write(raw['headers'] + '\n')
            f.write(raw['data'])
        return url_file
