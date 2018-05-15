# -*- coding:utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import os

class Bot:

    __slots__ = ['chat_enabled', 'share_enabled', 'remember_enabled', 'account', 'password', 'bot_name', 'need_train', 'train_data', 'auth_path']

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

    @qqbotslot
    def onQQMessage(self, bot, contact, member, content):
        
        # TODO 根据配置参数进行处理

        if not bot.isMe(contact, member):
            if member is not None:
                pass
            else:
                pass

    def isAuth(self, qq):
        user_auth_dict = self.loadAuthDict()
        if user_auth_dict is False:
            return False
        else:
            auth = user_auth_dict.get(qq,False)
        return auth

    def loadAuthDict(self):
        if os.path.exists(self.auth_path):
            with open(self.auth_path,'r') as f:
                user_auth_dict =  json.load(f)
            return user_auth_dict
        else:
            return False


    def __call__(self): 
        RunBot()