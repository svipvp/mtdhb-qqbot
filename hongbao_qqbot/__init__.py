# -*- config: utf-8 -*-

"""
    hongbao_qqbot
    -----------

    get max red packet everyday

    :copyright: © 2018 by the leetao.
    :license: GPL3.0,see LICENSE for more details
"""


__version__ = '0.0.1dev'

from .utils import generate_qqbot_config, get_qqbot_config
from .exception import *
from .hongbao import RedPackage
from .chat import Tuling