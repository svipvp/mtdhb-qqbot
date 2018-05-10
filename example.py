# -*- coding:utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot


class Bot:

    def __call__(self):
        RunBot()

    @qqbotslot
    def onQQMessage(self, bot, contact, member, content):
        if not bot.isMe(contact, member):
            if member is not None:
                print(member,contact,content)
            else:
                print(contact,content)



if __name__ == '__main__':
    bot = Bot()
    bot()