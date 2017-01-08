#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

import argparse
from utils.class_Wscanner import Wscanner

if __name__ == '__main__':

    parse = argparse.ArgumentParser(description="Wscanner, A another sqli scanner.")
    parse.add_argument('-p', '--project', type=int, dest="pid", default=0, help="Project that need to be scanned")
    args = parse.parse_args()

    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'hacksb',
        'db': 'Wscanner',
        'port': 3306,
        'charset': 'utf8'
    }
    scanner = Wscanner(db_config, args.pid)
    scanner.run()
