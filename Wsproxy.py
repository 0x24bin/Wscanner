#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

from lib.Wsproxy import *
import argparse

if __name__ == '__main__':

    parse = argparse.ArgumentParser(description="Wscanner, A another sqli scanner.")
    parse.add_argument('-p', '--project', type=int, dest="pid", default=0, help="Project that need to be scanned")
    args = parse.parse_args()

    # Wsproxy Config
    opts = options.Options(cadir="~/.mitmproxy/")
    config = ProxyConfig(opts)
    server = ProxyServer(config)
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'hacksb',
        'db': 'Wscanner',
        'port': 3306,
        'charset': 'utf8'
    }
    # run Wsproxy
    m = Wsproxy(opts, server, args.pid, db_config)
    m.run()
