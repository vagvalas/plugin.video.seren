# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

import sys

from resources.lib.common import tools

if tools.is_stub():
    # noinspection PyUnresolvedReferences
    from mock_kodi import MOCK

from resources.lib.modules import router
from resources.lib.modules.globals import g
from resources.lib.modules.timeLogger import TimeLogger

g.init_globals(sys.argv)

try:
    g.init_globals(sys.argv)
    if g.PLATFORM == "android" and g.get_bool_runtime_setting("system.sleeping", False):
        g.log(
            "Ignoring {} plugin action as system is supposed to be \"sleeping\".".format(
                g.REQUEST_PARAMS.get('action', '')
            ),
            "info"
        )
    else:
        with TimeLogger('{}'.format(g.REQUEST_PARAMS.get('action', ''))):
            router.dispatch(g.REQUEST_PARAMS)
finally:
    g.deinit()
