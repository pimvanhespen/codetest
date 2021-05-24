# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `Response.ice'
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

_M_Codetest._t_Response = IcePy.defineValue('::Codetest::Response', Ice.Value, -1, (), False, True, None, ())

if 'ResponsePrx' not in _M_Codetest.__dict__:
    _M_Codetest.ResponsePrx = Ice.createTempClass()
    class ResponsePrx(Ice.ObjectPrx):

        def GetResponse(self, context=None):
            return _M_Codetest.Response._op_GetResponse.invoke(self, ((), context))

        def GetResponseAsync(self, context=None):
            return _M_Codetest.Response._op_GetResponse.invokeAsync(self, ((), context))

        def begin_GetResponse(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Codetest.Response._op_GetResponse.begin(self, ((), _response, _ex, _sent, context))

        def end_GetResponse(self, _r):
            return _M_Codetest.Response._op_GetResponse.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Codetest.ResponsePrx.ice_checkedCast(proxy, '::Codetest::Response', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Codetest.ResponsePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Codetest::Response'
    _M_Codetest._t_ResponsePrx = IcePy.defineProxy('::Codetest::Response', ResponsePrx)

    _M_Codetest.ResponsePrx = ResponsePrx
    del ResponsePrx

    _M_Codetest.Response = Ice.createTempClass()
    class Response(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Codetest::Response', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Codetest::Response'

        @staticmethod
        def ice_staticId():
            return '::Codetest::Response'

        def GetResponse(self, current=None):
            raise NotImplementedError("servant method 'GetResponse' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Codetest._t_ResponseDisp)

        __repr__ = __str__

    _M_Codetest._t_ResponseDisp = IcePy.defineClass('::Codetest::Response', Response, (), None, ())
    Response._ice_type = _M_Codetest._t_ResponseDisp

    Response._op_GetResponse = IcePy.Operation('GetResponse', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_Codetest.Response = Response
    del Response

# End of module Codetest