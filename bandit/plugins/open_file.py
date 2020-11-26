# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id('B322')
@test.checks('Call')
def open_file(context):
    if context.call_function_name_qual == 'open':
        return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="open_file",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )
