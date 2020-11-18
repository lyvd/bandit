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

    sets.append(utils.build_conf_dict(
        'base64_b64decode', 'B300', ['base64.b64decode'],
        'base64.b64decode'
        ))

    sets.append(utils.build_conf_dict(
        'base64_b64encode', 'B301', ['base64.b64encode'],
        'base64.b64encode'
        ))

    #examples/socket_gethostname.py
    sets.append(utils.build_conf_dict(
        'socket_gethostname', 'B302', ['socket.gethostname'],
        'socket.gethostname'
        ))

    #examples/socket_gethostname.py
    sets.append(utils.build_conf_dict(
        'pwd_getpwuid', 'B303', ['pwd.getpwuid'],
        'pwd.getpwuid'
        ))

    #examples/socket_socket.py
    sets.append(utils.build_conf_dict(
        'socket_socket', 'B304', ['socket.socket'],
        'socket.socket'
        ))

    #examples/os_getuid.py
    sets.append(utils.build_conf_dict(
        'os_getuid', 'B305', ['os.getuid'],
        'os.getuid'
        ))

    #examples/zlib_decompress.py
    sets.append(utils.build_conf_dict(
        'zlib_decompress', 'B306', ['zlib.decompress'],
        'zlib.decompress'
        ))

    #examples/urllib_request_urlopen.py
    sets.append(utils.build_conf_dict(
        'urllib_request', 'B307', ['urllib.request'],
        'urllib.request'
        ))

    #examples/urllib_request_urlopen.py
    sets.append(utils.build_conf_dict(
        'urllib_request', 'B308', ['platform.system'],
        'platform.system'
        ))


    return {'Call': sets}
