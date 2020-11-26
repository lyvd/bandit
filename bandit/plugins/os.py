import bandit
from bandit.core import test_properties as test


@test.test_id('B813')
@test.checks('Str')
#@test.checks('Call')
def os_environ(context):
    if context.is_module_imported_like('os'):
        #qualname_list = context.call_function_name_qual.split('.')
        if  "environ" in context.call_function_name:
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="os.environ",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

