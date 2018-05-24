# -*- coding: utf-8 -*-

"""
    hongbao_qqbot.exception
    -----------

    Implements various exceptions

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""


class Error(Exception):
    """
        配置相关异常的基类
    """

    def __init__(self, msg=''):
        self.message = msg
        Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__


class ConfigNotFoundError(Error):
    """
        当配置不存在时抛出异常
    """

    def __init__(self, path=''):
        Error.__init__(self, "配置文件 %r 不存在" % (path,))
        self.path = path
        self.args = (path,)


class ConfigParamTypeError(Error):
    """
        参数类型错时抛出异常
    """

    def __init__(self, params, param_type):
        msg = ["参数类型错误: ", repr(params), " 不是 ", repr(param_type)]
        Error.__init__(self, "".join(msg))
        self.params = params
        self.param_type = param_type
        self.args = (params, param_type)


class NoOptionError(Error):
    """
        文件中不存在相关配置抛出异常
    """

    def __init__(self, option, section):
        Error.__init__(self, "%r 中不存在 %r 的配置" % (section, option))
        self.option = option
        self.section = section
        self.args = (option, section)


class NoSectionError(Error):
    """
        文件中不存在相关部分的时候抛出异常
    """

    def __init__(self, section):
        Error.__init__(self, "不存在有关 %r 的配置" % (section))
        self.section = section
        self.args = (section,)


class ApiNotFoundError(Error):
    """
        没有找到相应api的时候抛出异常
    """

    def __init__(self, key):
        Error.__init__(self, "没有找到 %r 对应的 api" % (key,))
        self.key = key
        self.args = (key,)

class DBConnectError(Error):
    """
        数据库连接错误时抛出异常
    """

    def __init__(self, e):
        Error.__init__(self," %r " %(e,))
        self.e = e
        self.args = (e,)