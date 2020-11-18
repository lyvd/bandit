import bandit
from bandit.core import test_properties as test


@test.test_id('B202')
@test.checks('Call')
def socket_socket_connect(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.connect'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="Connect to a remote socket at address",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B203')
@test.checks('Call')
def socket_send(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.send'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="Send data to the socket",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B204')
@test.checks('Call')
def socket_sendall(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.sendall'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="Send data to the socket",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )

@test.test_id('B205')
@test.checks('Call')
def socket_recv(context):
    if context.is_module_imported_like('socket'):
        if context.call_function_name_qual.endswith('.recv'):
            return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="Receive data from the socket.",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )


