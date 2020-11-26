# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id('B323')
@test.checks('Call')
def write_file(context):
    if context.call_function_name_qual.endswith('write'):
        import pdb; pdb.set_trace()
        return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="write_file",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )
