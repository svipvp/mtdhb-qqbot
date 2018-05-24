# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.chat
    -----------

    chat with you

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""

import requests
import json


class Tuling:
    def __init__(self):
        self.apiKey = '44c0dbf6a1d649c4bd6bf131525ccc03'
        self.requestUrl = "http://www.tuling123.com/openapi/api"

    def response(self, info, userid):
        param = {"key": self.apiKey, "info": info, "userid": userid}
        res = requests.post(self.requestUrl, params=param)
        obj = json.loads(res.text)
        codeStatus, msg = self.handle_Status(obj['code'])
        if codeStatus:
            text = obj['text']
            return text
        else:
            return msg

    def handle_Status(self, code):
        if code == '40001':
            return False, "内部出现点小问题"
        elif code == '40002':
            return False, "请求内容info为空"
        elif code == '40004':
            return False, "今天次数已经使用完"
        elif code == '40007':
            return False, "数据格式异常"
        else:
            return True, None