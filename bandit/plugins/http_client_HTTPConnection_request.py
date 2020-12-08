# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id("B325")
@test.checks("Call")
def http_client_HTTPConnection_request(context):
    if context.is_module_imported_like("http"):
        if context.call_function_name_qual.endswith("request"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="http.client.HTTPConnection.request",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
