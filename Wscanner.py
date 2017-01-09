#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

import time
import argparse
import threading
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

    for i in range(10):
        t = threading.Thread(target=scanner.run)
        t.setDaemon(True)
        t.start()

    while True:
        if threading.activeCount() <= 1:
            break
        else:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt, e:
                print '\n[WARNING] User aborted, wait all slave threads to exit, current(%i)' % threading.activeCount()
                scanner.STOP_ME = True

    print "Scan End!"
