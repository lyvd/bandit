# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B331")
@test.checks("Call")
def http_server_HTTPServer(context):
    if context.is_module_imported_like("http"):
        if context.call_function_name_qual.endswith("HTTPServer"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="http.server.HTTPServer",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
