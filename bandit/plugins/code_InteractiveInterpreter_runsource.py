# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B345")
@test.checks("Call")
def code_InteractiveInterpreter_runsource(context):
    if context.is_module_imported_like("code"):
        if context.call_function_name_qual.endswith("runsource"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="code_InteractiveInterpreter_runsource",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
