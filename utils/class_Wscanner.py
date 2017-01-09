#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

import os
import Queue
import threading
from utils.WsproxyDb import *
from utils.class_Sqlmap import SqlmapApi


class Wscanner(object):

    STOP_ME = False

    def __init__(self, db_config, pid):
        self.pid = pid
        self.db_config = db_config
        self.wsdb = WsproxyDb(self.db_config, self.pid)
        self.sqlmap_api = SqlmapApi()
        self._load_target()
        self.lock = threading.Lock()

    def run(self):
        while not self.target.empty() and self.STOP_ME is False:
            target = self.target.get()
            self._run(target)

    def _run(self, target):
        # new
        self.lock.acquire()
        url_file = self.get_url_file(target)
        self.lock.release()

        self.lock.acquire()
        self.wsdb.update_url_status(target['id'], 1)
        self.lock.release()

        print "[Scanning]: %s" % target['url']
        if self.sqlmap_api.start(url_file):
            self.lock.acquire()
            self.wsdb.update_url_status(target['id'], 2)
            self.lock.release()
            print "\033[1;31m[VULN]: %s\033[0m" % target['url']
        else:
            self.lock.acquire()
            self.wsdb.update_url_status(target['id'], 3)
            self.lock.release()
            print "[NO_VULN] :%s" % target['url']

        # old
        # raw = self.wsdb.get_url(0)
        # self.URL_ID = raw['id']
        # url_file = self.get_url_file(raw)
        # self.wsdb.update_url_status(self.URL_ID, 1)
        # print "[Scanning]: %s" % raw['url']
        # if self.sqlmap_api.start(url_file):
        #     self.wsdb.update_url_status(self.URL_ID, 2)
        #     print "\033[1;31m[VULN]: %s\033[0m" % raw['url']
        # else:
        #     self.wsdb.update_url_status(self.URL_ID, 3)
        #     print "[NO_VULN] :%s" % raw['url']

    def _load_target(self):
        self.target = Queue.Queue()
        target = self.wsdb.get_url(self.pid, 0)
        for line in target:
            self.target.put(line)
        print "loaded %s target" % self.target.qsize()

    @staticmethod
    def get_url_file(raw):
        url_file = os.getcwd() + '/tmp/url_' + str(raw['id']) + '.txt'
        with open(url_file, 'w') as f:
            f.write(raw['method'] + ' ' + raw['url'] + ' HTTP/1.1' + '\n')
            f.write(raw['headers'] + '\n')
            f.write(raw['data'])
        return url_file
