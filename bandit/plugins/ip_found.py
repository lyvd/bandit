import bandit
import re
from bandit.core import test_properties as test

@test.checks('Str')
@test.test_id('B501')
def ip_found(context):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", context.string_val):
        return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.MEDIUM,
            text="ip_found"
        )
