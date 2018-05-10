# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.hongbao
    -----------

    get max hongbao for you

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""

from .exception import ApiNotFoundError

import requests

api_dict = {
    "get_notice": 'notice.json',
    "login": "user/login",
    "logout": "user/logout",
    "get_hongbao": "user/receiving"
}


def _get_url_wrapper(func):
    def wrapper(self, **kwargs):
        api = api_dict.get(func.__name__, None)
        if api is None:
            raise ApiNotFoundError(func.__name__)
        kwargs['api'] = api
        return func(self, **kwargs)

    return wrapper


class RedPackage:
    __slots__ = ['account', 'password', 'domain', 'api_dict', 'token']

    def __init__(self, account, password, domain=None):

        self.account = account
        self.password = password
        self.token = None

        self.domain = domain if domain is not None else 'https://api.mtdhb.com/'

    @_get_url_wrapper
    def login(self, **kwargs):
        url = self.domain + kwargs.get('api')
        payload = {
            "account": self.account,
            "password": self.password
        }
        res = requests.post(url, data=payload)
        resObj = res.json()
        if resObj['message'] is None and resObj['code'] == 0:
            self.token = resObj['data']['token']
            return True, '登陆成功'
        else:
            return False, resObj['message']

    @_get_url_wrapper
    def get_hongbao(self, **kwargs):
        if self.token is None:
            return False, "暂未登陆,请先登陆后尝试领取红包"
        url = self.domain + kwargs.get('api')
        headers = {"x-user-token": self.token}
        payload = {"phone": kwargs.get('phone'), "url": kwargs.get('url')}
        res = requests.post(url, headers=headers, data=payload)
        resObj = res.json()
        return resObj['message']

    @_get_url_wrapper
    def logout(self, **kwargs):
        if self.token is None:
            return False, "您已经处于退出状态"
        url = self.domain + kwargs.get('api')
        headers = {"x-user-token": self.token}
        res = requests.get(url, headers=headers)
        resObj = res.json()
        if resObj['code'] == 0:
            return "成功退出登陆"
        else:
            return resObj['message']