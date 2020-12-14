# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B337")
@test.checks("Call")
def shutil_rmtree(context):
    if context.is_module_imported_like("shutil"):
        if context.call_function_name_qual.endswith("rmtree"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="shutil_rmtree",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
