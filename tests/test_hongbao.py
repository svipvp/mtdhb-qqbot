# -*- coding: utf-8 -*-

"""
    tests.test_hongbao
    -----------

    Tests hongbao_qqbot.hongbao

    :copyright: © 2018 by leetao
    :license: GPL3.0, see LICENSE for more details.
"""

from hongbao_qqbot import RedPackage


import pytest

def test_login():

    red_package = RedPackage('501257367@qq.com','xxxx')
    flag,message = red_package.login()
    assert flag is False

    red_package = RedPackage('501257367@qq.com','556633abc')
    flag,message = red_package.login()
    assert flag is True