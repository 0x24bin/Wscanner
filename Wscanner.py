#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""

import sys
import os
sys.path.insert(0, os.getcwd()+'/lib/sqlmap/')
import sqlmap as sqlmap_api

# TODO:取出url保存到tmp目录

# 运行sqlmap
sqlmap_api.main()

