# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B332")
@test.checks("Call")
def os_read(context):
    if context.is_module_imported_like("os"):
        if context.call_function_name_qual.endswith("read"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="os_read",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
