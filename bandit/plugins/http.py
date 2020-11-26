import bandit
from bandit.core import test_properties as test


@test.test_id('B713')
@test.checks('Call')
def http_client(context):
    if context.is_module_imported_like('http'):
        qualname_list = context.call_function_name_qual.split('.')
        middle_func = qualname_list[1]
        if middle_func == "client":
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="http.client",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

