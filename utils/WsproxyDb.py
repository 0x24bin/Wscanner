#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
    WScanner, another sql injection scanner
    Author: 王松_Striker <song@secbox.cn>

"""
import re
import pymysql.cursors


class WsproxyDb(object):

    def __init__(self, db_config, pid):
        self.sql = None
        self.data = dict()
        self.pid = pid
        self.db_config = db_config
        for key, value in self.db_config.items():
            setattr(self, key, value)
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              db=self.db,
                                              charset=self.charset,
                                              cursorclass=pymysql.cursors.DictCursor
                                              )
        except pymysql.err.OperationalError:
            print('Mysql connect error, Please check your mysql config.')
            quit()

    def update_url_status(self, url_id, status):
        with self.connection.cursor() as cursor:
            self.sql = "update ws_url set sqli=%s where id=%s"
            cursor.execute(self.sql, (status, url_id))
        self.connection.commit()
        cursor.close()

    def get_url(self, pid, sqli):
        with self.connection.cursor() as cursor:
            self.sql = "select * from ws_url where sqli=%s and pid=%s"
            cursor.execute(self.sql, (sqli, pid))
            result = cursor.fetchall()
            return result

    def log_url(self, request):
        # 检查url有效性,有效则入库
        if self.check_url(request):
            self.data['pid'] = self.pid
            self.data['method'] = request.method
            self.data['url'] = request.url
            self.data['data'] = request.content
            self.data['headers'] = bytes(request.headers)
            with self.connection.cursor() as cursor:
                self.sql = "insert into ws_url(pid, method, url, data, headers) values (%s, %s, %s, %s, %s)"
                cursor.execute(self.sql, (self.data['pid'], self.data['method'], self.data['url'], self.data['data'], self.data['headers']))
            self.connection.commit()
            cursor.close()

    @staticmethod
    def check_url(request):
        # 检查是否是静态资源
        ext_list = ['css', 'js', 'gif', 'jpg', 'png', 'ico', 'txt', 'pdf', 'zip', 'rar', 'gz', 'cs']
        no_param_url = request.url.split('?')[0]
        pattern = re.compile(r"https?://.*/.*\.(.*)")
        res = pattern.match(no_param_url)
        if res:
            ext = res.groups()[0]
        else:
            ext = None
        # 如果是静态资源则返回
        if ext in ext_list:
            return False

        # 没有请求参数且是GET请求
        if len(request.url.split('?')) == 1 and request.method == "GET":
            return False

        # 上面都通过了则返回true
        return True
