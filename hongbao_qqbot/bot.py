# -*- coding:utf-8 -*-

"""
    hongbao_qqbot.bot
    -----------

    the core of hongbao qqbot

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""

import os
import re
from .chat import Tuling
from .db import DB
from .hongbao import RedPackage


class Bot:
    __slots__ = ['chat_enabled', 'chat', 'hongbao_db', 'hongbao', 'basedir']

    def __init__(self, **kwargs):
        self.chat_enabled = kwargs.get('chat_enabled', False)
        self.chat = Tuling()
        self.basedir = kwargs.get("basedir", os.path.join(os.path.abspath(os.path.dirname(__file__))))
        self.hongbao_db = DB(os.path.join(self.basedir, '../database/hongbao.db'))
        self.hongbao = RedPackage()

    def onQQMessage(self, bot, contact, member, content):
        url_flag, phone_flag = self.check_content(content)
        if (not url_flag and not phone_flag) is True:
            if self.chat_enabled:
                text = self.chat.response(member.name, content)
                bot.SendTo(contact, "@{0}:{1}".format(contact.name, text))
            else:
                bot.SendTo(contact, "@{0}:{1}".format(contact.name, "小主暂未开启聊天功能😭"))
        else:
            message = self.handle_check_status(url_flag, phone_flag, contact, member, content)
            bot.SendTo(contact, "@{0}:{1}".format(contact.name, message))

    def handle_check_status(self, url_flag, phone_flag, contact, member, content):
        if url_flag:
            flag = self.hongbao_db.insert_package_url(contact.qq, content)
            if flag:
                return '请输入您的手机号'
            return '发生了未知错误'
        if phone_flag:
            if self.isAuth(contact) is False:
                return '请先登录后再尝试领取红包'
            else:
                return self.get_red_package(contact, member, content)

    def get_red_package(self, contact, member, phone):
        """
        get max package
        
        根据 qq 号获取最近一条提交的红包链接
        
        :param bot
        :param contact
        :param phone
        """

        url = self.hongbao_db.get_package_url(phone)
        if url is None:
            return '请先分享您的红包链接'
        return self.hongbao.get_hongbao(phone=phone, url=url)

    def check_content(self, content):
        """
        check content
        依次检测内容是否为外卖链接和手机号
        :param content
        :return bool
        """
        url_flag, _ = self._check_url_format(content)
        phone_flag, _ = self._check_phone_format(content)
        return url_flag, phone_flag

    def _check_url_format(self, url):
        """
        check url format
        :param url
        :return bool,status_code
        """
        if url[:5] == 'https':
            if url.find('https://activity.waimai.meituan.com/') != -1 or url.find('https://h5.ele.me/hongbao/') != -1:
                return True, '403'
            else:
                return False, '402'
        return False, '404'

    def _check_phone_format(self, phone):
        """
        check phone number format
        :param phone
        :return bool,status_code
        """
        pattern = re.compile(
            '^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$')
        if_match = pattern.match(phone)
        if if_match:
            return True, None
        return False, '404'

    def isAuth(self, contact):
        """
        check if the user login
        :param contact
        :return bool or token
        """
        if contact.qq != '#NULL':
            qq = contact.qq
        else:
            qq = contact.name
        return self.hongbao_db.is_auth(qq)
