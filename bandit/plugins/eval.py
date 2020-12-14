
import six

import bandit
from bandit.core import test_properties as test


def eval_issue():
    return bandit.Issue(severity=bandit.MEDIUM, confidence=bandit.HIGH, text="eval")


@test.test_id("B347")
@test.checks("Call")
def eval_used(context):
    if context.call_function_name_qual == "eval":
        return eval_issue()
