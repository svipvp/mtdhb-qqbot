# -*- coding:utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot


class Bot:

    __slots__ = ['chat_enabled', 'share_enabled', 'remember_enabled', 'account', 'password', 'bot_name', 'need_train', 'train_data']

    def __init__(self, **kwargs):
        self.chat_enabled = kwargs.get('chat_enabled', False)
        self.share_enabled = kwargs.get('share_enabled', False)
        self.remember_enabled = kwargs.get('remember_enabled', True)
        self.account = kwargs.get('account', '*')
        self.password = kwargs.get('password', '*')
        self.bot_name = kwargs.get('bot_name', 'mtdhb')
        self.need_train = kwargs.get('need_train', False)
        self.train_data = kwargs.get('train_data', '*')


    @qqbotslot
    def onQQMessage(self, bot, contact, member, content):
        
        # TODO 根据配置参数进行处理

        if not bot.isMe(contact, member):
            if member is not None:
                pass
            else:
                pass

    def __call__(self): 
        RunBot()