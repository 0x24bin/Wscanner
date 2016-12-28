#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

from mitmproxy.proxy import ProxyServer, ProxyConfig
from mitmproxy import controller, options, master
from lib.WsproxyDb import *


class Wsproxy(master.Master):
    def __init__(self, myopts, myserver, pid, db_config):
        super(Wsproxy, self).__init__(myopts, myserver)
        self.pid = pid
        self.db_config = db_config
        self.wsdb = WsproxyDb(self.db_config, self.pid)

    def run(self):
        try:
            print("Wsproxy pid is", self.pid)
            print("Wsproxy is running!")
            master.Master.run(self)
        except KeyboardInterrupt:
            self.wsdb.connection.close()
            self.shutdown()

    @controller.handler
    def request(self, f):
        print("Wsproxy", "[", f.request.method, "]", f.request.url)
        # 调用WsproxyDb存入数据库
        # TODO：过滤静态资源
        self.wsdb.log_url(f.request)
