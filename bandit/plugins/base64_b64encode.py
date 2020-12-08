# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B301")
@test.checks("Call")
def base64_b64encode(context):
    if context.is_module_imported_like("base64"):
        if context.call_function_name_qual.endswith("b64encode"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="base64.b64encode",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
