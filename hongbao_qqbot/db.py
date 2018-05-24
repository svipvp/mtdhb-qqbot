# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.db
    -----------

    operate sqlite with db

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""

import sqlite3
from exception import DBConnectError

class DB:

    __slots__ = ['_cur']

    def __init__(self, db_path):
        try:
            conn = sqlite3.connect(db_path)
            self._cur = conn.cursor()
        except Exception as e:
            raise DBConnectError(e)
    
    def insert_token(self, qq, token):
        pass

    def get_token(self, qq):
        pass
    
    def insert_package_url(self, qq, url):
        pass

    def get_package_url(self, qq):
        pass