# -*- coding: utf-8 -*-

"""
    tests.test_utils
    -----------

    Tests hongbao_qqbot.utils

    :copyright: © 2018 by leetao
    :license: GPL3.0, see LICENSE for more details.
"""

from hongbao_qqbot import generate_qqbot_config, get_qqbot_config, ConfigNotFoundError

import pytest
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


def test_generate_qqbot_config():
    generate_qqbot_config()
    assert os.path.exists('qqbot.cfg') is True

    config_path = os.path.join(base_dir, "test_config")
    generate_qqbot_config(config_path)
    assert os.path.exists(os.path.join(config_path, "qqbot.cfg")) is True


def test_get_qqbot_config():
    with pytest.raises(ConfigNotFoundError):
        get_qqbot_config("")

    config_path = os.path.join(base_dir, "test_config")
    config_dict = get_qqbot_config(os.path.join(config_path,'qqbot.cfg'))
    test_config_dict_right_keys = ['chat_enabled', 'share_enabled', 'remember_enabled', 'account', 'password',
                                   'bot_name', 'need_train', 'train_data']
    assert all(map(lambda x: x in config_dict, test_config_dict_right_keys)) is True

    test_config_dict_error_keys = ['chat_enabled', 'share_enabled', 'remember_enabled', 'account', 'password',
                                   'error_bot_name', 'need_train', 'train_data']
    assert all(map(lambda x: x in config_dict, test_config_dict_error_keys)) is False