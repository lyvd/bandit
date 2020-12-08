import bandit
from bandit.core import test_properties as test


@test.checks("Call")
@test.test_id("B612")
def b64decode_calls(context):
    issue_text = "decode data using base64 "
    for module in ["base64"]:
        if context.is_module_imported_like(module):
            if context.call_function_name in ["b64decode"]:
                return bandit.Issue(severity=bandit.MEDIUM, confidence=bandit.MEDIUM, text=issue_text)
