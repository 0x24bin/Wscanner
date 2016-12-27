#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""


from mitmproxy import controller, options, master
from mitmproxy.proxy import ProxyServer, ProxyConfig
import argparse


class Wsproxy(master.Master):
    def __init__(self, myopts, myserver, pid):
        super(Wsproxy, self).__init__(myopts, myserver)
        print("Wsproxy pid is", pid)

    def run(self):
        try:
            print("Wsproxy is running!")
            master.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    @controller.handler
    def request(self, f):
        print("Wsproxy", "[", f.request.method, "]", f.request.url)


if __name__ == '__main__':

    parse = argparse.ArgumentParser(description="Wscanner, A another sqli scanner.")
    parse.add_argument('-p', '--project', type=int, dest="pid", default=0, help="Project that need to be scanned")
    args = parse.parse_args()

    # Wsproxy Config
    opts = options.Options(cadir="~/.mitmproxy/")
    config = ProxyConfig(opts)
    server = ProxyServer(config)
    m = Wsproxy(opts, server, args.pid)
    # run Wsproxy
    m.run()
