#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class SqlmapApi(object):

    VULN_STR = "[INFO] the back-end DBMS is"
    NOT_VULN_STR = 'all tested parameters appear to be not injectable'
    SQLMAP_RESULT = ''
    SQLMAP_PARAM = ''

    def __init__(self):
        self.SQLMAP_PATH = os.getcwd() + '/utils/sqlmap/sqlmap.py'

    def start(self, url_file):
        self.SQLMAP_PARAM = "-r " + url_file + " --batch --risk 3"
        cmd = "python %s %s" % (self.SQLMAP_PATH, self.SQLMAP_PARAM)
        self.SQLMAP_RESULT = os.popen(cmd).read()

        if self.VULN_STR in self.SQLMAP_RESULT and self.NOT_VULN_STR not in self.SQLMAP_RESULT:
            return True
        else:
            return False
