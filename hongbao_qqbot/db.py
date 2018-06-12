# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.db
    -----------

    operate sqlite with db

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""
import sqlite3

from .exception import DBConnectError


class DB:
    __slots__ = ['conn']

    def __init__(self, db_path):
        try:
            self.conn = sqlite3.connect(db_path)
        except Exception as e:
            raise DBConnectError(e)

    def insert_token(self, qq, token):
        try:
            with self.conn:
                row_count = self.conn.execute("INSERT INTO users(qq, token) VALUES (?, ?)", (qq, token)).rowcount
                return True if row_count > 0 else False
        except Exception as e:
            print(e)
            return False
        return True

    def get_token(self, qq):
        try:
            with self.conn:
                row = self.conn.execute("SELECT token FROM users WHERE qq = ?", (qq,)).fetchone()
                return row[0]
        except Exception as e:
            print(e)
            return None

    def is_auth(self, qq):
        try:
            with self.conn:
                row = self.conn.execute("SELECT token FROM users WHERE qq = ?", (qq,)).fetchone()
                return True if row[0] is not None else False
        except Exception as e:
            print(e)
            return None

    def insert_package_url(self, qq, url):
        try:
            with self.conn:
                row_count = self.conn.execute("INSERT INTO packages(qq,url) VALUES (?,?)", (qq, url)).rowcount
                return True if row_count > 0 else False
        except Exception as e:
            print(e)
            return False

    def get_package_url(self, qq, status=0):
        try:
            with self.conn:
                row = self.conn.execute("SELECT url FROM packages WHERE qq = ? AND status = ?", (qq, status)).fetchone()
                return row[0]
        except Exception as e:
            print(e)
            return None
