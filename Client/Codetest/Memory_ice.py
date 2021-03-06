# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `Memory.ice'
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

_M_Codetest._t_Memory = IcePy.defineValue('::Codetest::Memory', Ice.Value, -1, (), False, True, None, ())

if 'MemoryPrx' not in _M_Codetest.__dict__:
    _M_Codetest.MemoryPrx = Ice.createTempClass()
    class MemoryPrx(Ice.ObjectPrx):

        def GetFreeMemory(self, context=None):
            return _M_Codetest.Memory._op_GetFreeMemory.invoke(self, ((), context))

        def GetFreeMemoryAsync(self, context=None):
            return _M_Codetest.Memory._op_GetFreeMemory.invokeAsync(self, ((), context))

        def begin_GetFreeMemory(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Codetest.Memory._op_GetFreeMemory.begin(self, ((), _response, _ex, _sent, context))

        def end_GetFreeMemory(self, _r):
            return _M_Codetest.Memory._op_GetFreeMemory.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Codetest.MemoryPrx.ice_checkedCast(proxy, '::Codetest::Memory', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Codetest.MemoryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Codetest::Memory'
    _M_Codetest._t_MemoryPrx = IcePy.defineProxy('::Codetest::Memory', MemoryPrx)

    _M_Codetest.MemoryPrx = MemoryPrx
    del MemoryPrx

    _M_Codetest.Memory = Ice.createTempClass()
    class Memory(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Codetest::Memory', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Codetest::Memory'

        @staticmethod
        def ice_staticId():
            return '::Codetest::Memory'

        def GetFreeMemory(self, current=None):
            raise NotImplementedError("servant method 'GetFreeMemory' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Codetest._t_MemoryDisp)

        __repr__ = __str__

    _M_Codetest._t_MemoryDisp = IcePy.defineClass('::Codetest::Memory', Memory, (), None, ())
    Memory._ice_type = _M_Codetest._t_MemoryDisp

    Memory._op_GetFreeMemory = IcePy.Operation('GetFreeMemory', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_long, False, 0), ())

    _M_Codetest.Memory = Memory
    del Memory

# End of module Codetest
