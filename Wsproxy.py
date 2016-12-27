#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""


from mitmproxy import controller, options, master
from mitmproxy.proxy import ProxyServer, ProxyConfig


class Wsproxy(master.Master):
    def run(self):
        try:
            print("Wsproxy is running!")
            master.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    @controller.handler
    def request(self, f):
        print("Wsproxy", "[", f.request.method, "]", f.request.url)

opts = options.Options(cadir="/tmp/Wsproxy/")
config = ProxyConfig(opts)
server = ProxyServer(config)
m = Wsproxy(opts, server)
m.run()
