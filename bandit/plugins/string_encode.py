import bandit
import re
import ast
from bandit.core import test_properties as test

@test.checks('Str')
@test.test_id('B503')
def string_encode(context):
    #import pdb; pdb.set_trace()
    if isinstance(context.node._bandit_parent, ast.Attribute):
        if context.node._bandit_parent.attr == 'encode':
            return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.MEDIUM,
            text="string_encode"
        )
