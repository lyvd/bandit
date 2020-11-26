
import bandit
from bandit.core import test_properties as test


@test.checks('Call')
@test.test_id('B500')
def b64decode_calls(context):
    issue_text = ('')
    for module in ['urllib']:
        if context.is_module_imported_like(module):
            if context.call_function_name in ['urlopen']:
                return bandit.Issue(severity=bandit.MEDIUM,
                                    confidence=bandit.MEDIUM,
                                    text=issue_text)
