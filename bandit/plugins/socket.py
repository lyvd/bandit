# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id('B309')
@test.checks('Call')
def socket_socket_connect(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.connect'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="socket.socket.connect",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B310')
@test.checks('Call')
def socket_socket_send(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.send'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="socket.socket.send",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B311')
@test.checks('Call')
def socket_socket_sendall(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.sendall'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="socket.socket.sendall",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B312')
@test.checks('Call')
def socket_socket_recv(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.recv'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="socket.socket.recv.",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )
