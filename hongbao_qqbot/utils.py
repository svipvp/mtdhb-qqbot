# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.utils
    -----------

    Implements various utils

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""

import configparser

import os

from .exception import NoOptionError, NoSectionError, ConfigParamTypeError, ConfigNotFoundError


def _get_config(path, config_dict):
    """
        根据配置文件路径以及配置列表返回相关配置

        :return dict
    """

    config_value_dict = {}

    cp = configparser.ConfigParser()

    if os.path.exists(path):
        cp.read(path)
        if isinstance(config_dict, dict):
            for key, value in config_dict.items():
                if isinstance(value, list):
                    try:
                        for item in value:
                            config_value_dict[item] = cp.get(key, item)
                    except configparser.NoSectionError:
                        raise NoSectionError(key)
                    except configparser.NoOptionError:
                        raise NoOptionError(key, item)
                elif isinstance(value, str):
                    config_value_dict[value] = cp.get(key, value)
                else:
                    raise ConfigParamTypeError(value, 'str or list')
        else:
            raise ConfigParamTypeError(config_dict, dict)
    else:
        raise ConfigNotFoundError(path)
    return config_value_dict


def get_qqbot_config(path):
    """
        获取配置文件的所有配置

        获取 DEFAULT 配置
        获取 PERSONAL 配置如果有的话
        获取 CHATBOT 配置如果有的话
    """
    pass


def generate_qqbot_config(path=None):
    """
        生成默认配置文件
        如果没有指定路径则在当前目录生成 qqbot.cfg 文件
    """
    cp = configparser.ConfigParser()

    # 添加 DEFAULT 部分    
    cp.set("DEFAULT", "chat_enabled", "True")
    cp.set("DEFAULT", "share_enabled", "False")
    cp.set("DEFAULT", "remember_enabled", "True")

    # 添加 PERSONAL 部分
    cp.add_section("PERSONAL")
    cp.set("PERSONAL", "account", "*")
    cp.set("PERSONAL", "password", "*")

    # 添加 PERSONAL 部分
    cp.add_section("CHATBOT")
    cp.set("CHATBOT", "bot_name", "mtdhb")
    cp.set("CHATBOT", "need_train", "False")
    cp.set("CHATBOT", "train_data", "*")

    if path is None:
        config_path = "qqbot.cfg"
    else:
        config_path = os.path.join(path, "qqbot.cfg")

    with open(config_path, "w+") as f:
        cp.write(f)


STAUS_CODE = {
    "401": "未登陆",
    "402": "请确保,饿了么是以https://h5.ele.me/hongbao/开头的链接,美团是以https://activity.waimai.meituan.com/开头的链接",
    "403": "输入手机号号码",
    "404": "手机号码有误"
}