import bandit
from bandit.core import test_properties as test


@test.test_id("B313")
@test.checks("Call")
def urllib_request_urlopen(context):
    if context.is_module_imported_like("urllib"):
        if context.call_function_name_qual.endswith(".urlopen"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="urllib.request.urlopen",
                lineno=context.get_lineno_for_call_arg("debug"),
            )


@test.test_id("B314")
@test.checks("Call")
def urllib_request_Request(context):
    if context.is_module_imported_like("urllib"):
        if context.call_function_name_qual.endswith(".Request"):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.MEDIUM,
                text="urllib.request.Request",
                lineno=context.get_lineno_for_call_arg("debug"),
            )
