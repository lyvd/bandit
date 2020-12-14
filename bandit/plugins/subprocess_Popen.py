# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B341")
@test.checks("Call")
def subprocess_Popen(context):
    if context.is_module_imported_like("subprocess"):
        if context.call_function_name_qual.endswith("Popen"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="subprocess_Popen",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
