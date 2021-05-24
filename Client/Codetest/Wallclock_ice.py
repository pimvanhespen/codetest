# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `Wallclock.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Codetest
_M_Codetest = Ice.openModule('Codetest')
__name__ = 'Codetest'

_M_Codetest._t_Wallclock = IcePy.defineValue('::Codetest::Wallclock', Ice.Value, -1, (), False, True, None, ())

if 'WallclockPrx' not in _M_Codetest.__dict__:
    _M_Codetest.WallclockPrx = Ice.createTempClass()
    class WallclockPrx(Ice.ObjectPrx):

        def GetWallclockTime(self, context=None):
            return _M_Codetest.Wallclock._op_GetWallclockTime.invoke(self, ((), context))

        def GetWallclockTimeAsync(self, context=None):
            return _M_Codetest.Wallclock._op_GetWallclockTime.invokeAsync(self, ((), context))

        def begin_GetWallclockTime(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Codetest.Wallclock._op_GetWallclockTime.begin(self, ((), _response, _ex, _sent, context))

        def end_GetWallclockTime(self, _r):
            return _M_Codetest.Wallclock._op_GetWallclockTime.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Codetest.WallclockPrx.ice_checkedCast(proxy, '::Codetest::Wallclock', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Codetest.WallclockPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Codetest::Wallclock'
    _M_Codetest._t_WallclockPrx = IcePy.defineProxy('::Codetest::Wallclock', WallclockPrx)

    _M_Codetest.WallclockPrx = WallclockPrx
    del WallclockPrx

    _M_Codetest.Wallclock = Ice.createTempClass()
    class Wallclock(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Codetest::Wallclock', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Codetest::Wallclock'

        @staticmethod
        def ice_staticId():
            return '::Codetest::Wallclock'

        def GetWallclockTime(self, current=None):
            raise NotImplementedError("servant method 'GetWallclockTime' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Codetest._t_WallclockDisp)

        __repr__ = __str__

    _M_Codetest._t_WallclockDisp = IcePy.defineClass('::Codetest::Wallclock', Wallclock, (), None, ())
    Wallclock._ice_type = _M_Codetest._t_WallclockDisp

    Wallclock._op_GetWallclockTime = IcePy.Operation('GetWallclockTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), ())

    _M_Codetest.Wallclock = Wallclock
    del Wallclock

# End of module Codetest
