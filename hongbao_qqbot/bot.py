# -*- coding:utf-8 -*-

"""
    hongbao_qqbot.bot
    -----------

    the core of hongbao qqbot

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""


from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import os
from utils import STAUS_CODE
from chat import Tuling

class Bot:

    __slots__ = ['chat_enabled', 'share_enabled', 'remember_enabled', 'account',
                 'password', 'bot_name', 'need_train', 'train_data', 'auth_path', 'chat']

    def __init__(self, **kwargs):
        self.chat_enabled = kwargs.get('chat_enabled', False)
        self.share_enabled = kwargs.get('share_enabled', False)
        self.remember_enabled = kwargs.get('remember_enabled', True)
        self.account = kwargs.get('account', '*')
        self.password = kwargs.get('password', '*')
        self.bot_name = kwargs.get('bot_name', 'mtdhb')
        self.need_train = kwargs.get('need_train', False)
        self.train_data = kwargs.get('train_data', '*')
        self.auth_path = 'store.json'
        self.chat = Tuling()

    @qqbotslot
    def onQQMessage(self, bot, contact, member, content):
        
        if self.check_content(check_content):
            if self.chat_enabled:
                text = self.chat.response(member.name, content)
                bot.SendTo(contact, "@{0}:{1}".format(member.name, text))
            else:
                bot.SendTo(contact, "@{0}:{1}".format(member.name, "小主暂未开启聊天功能😭"))
        else:

        



    def get_red_package(self, bot, contact, content):
        """
        get max package
        分享红包链接,检测当前用户是否登陆,
        如果登陆要求输入手机号码
        没有登陆返回登陆信息

        # TODO 记录红包链接和qq号的对应关系
        
        :param bot
        :param contact
        :param content
        """
        if not bot.isMe(contact, member):
            if self.isAuth(contact) is False:
                return '401'
            else:
                pass
        return None

    def check_content(self, content):
        """
        check content
        判断内容是否为外卖链接和手机号
        :param content
        :return bool
        """
        url_flag, url_status_code = self._check_url_format(content)
        phone_flag, phone_status_code = self._check_phone_format(content)
        if url_flag is False and phone_flag is False:
            return True
        return False

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


    def _check_phone_format(self, phone):
        """
        check phone number format
        :param phone
        :return bool,status_code
        """
        pattern = re.compile(
            '^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$')
        if_match = pattern.match(phone)
        if phone:
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
        user_auth_dict = self.loadAuthDict()
        if user_auth_dict is False:
            return False
        else:
            auth = user_auth_dict.get(qq, False)
        return auth

    def loadAuthDict(self):
        """
        load auth dict
        :return dict
        """
        if os.path.exists(self.auth_path):
            with open(self.auth_path, 'r') as f:
                user_auth_dict = json.load(f)
            return user_auth_dict
        else:
            return False

    def __call__(self):
        RunBot()
