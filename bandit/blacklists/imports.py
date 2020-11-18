
from bandit.blacklists import utils


def gen_blacklist():
    """Generate a list of items to blacklist.

    Methods of this type, "bandit.blacklist" plugins, are used to build a list
    of items that bandit's built in blacklisting tests will use to trigger
    issues. They replace the older blacklist* test plugins and allow
    blacklisted items to have a unique bandit ID for filtering and profile
    usage.

    :return: a dictionary mapping node types to a list of blacklist data
    """

    sets = []

    # example: examples/import_base64
    sets.append(utils.build_conf_dict(
        'import_base64', 'B400', ['base64'],
        'import_base64',
        'HIGH'
        ))

    # example: examples/import_socket.py
    sets.append(utils.build_conf_dict(
        'import_socket', 'B401', ['socket'],
        'import_socket',
        'HIGH'
        ))

    # example: examples/import_zlib.py
    sets.append(utils.build_conf_dict(
        'import_zlib', 'B402', ['zlib'],
        'import_zlib',
        'HIGH'
        ))

    # example: examples/import_urllib.py
    sets.append(utils.build_conf_dict(
        'import_urllib', 'B403', ['urllib'],
        'import_urllib',
        'HIGH'
        ))

    # example: examples/import_urllib.py
    sets.append(utils.build_conf_dict(
        'import_pwd', 'B404', ['pwd'],
        'import_pwd',
        'HIGH'
        ))

    # example: examples/import_http.py
    sets.append(utils.build_conf_dict(
        'import_http', 'B405', ['http'],
        'import_http',
        'HIGH'
        ))

    # example: examples/import_platform.py
    sets.append(utils.build_conf_dict(
        'import_platform', 'B406', ['platform'],
        'import_platform',
        'HIGH'
        ))

    # example: examples/import_os.py
    sets.append(utils.build_conf_dict(
        'import_os', 'B407', ['os'],
        'import_os',
        'HIGH'
        ))

    # example: examples/import_socketserver.py
    sets.append(utils.build_conf_dict(
        'import_socketserver.', 'B408', ['socketserver'],
        'import_socketserver',
        'HIGH'
        ))
    return {'Import': sets, 'ImportFrom': sets, 'Call': sets}
