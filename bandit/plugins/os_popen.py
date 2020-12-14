# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B340")
@test.checks("Call")
def os_popen(context):
    if context.is_module_imported_like("os"):
        if context.call_function_name_qual.endswith("popen"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="os_popen",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
