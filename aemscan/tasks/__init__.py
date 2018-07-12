__author__ = 'raz0r'

from . import \
    get_version, \
    check_default_error_page, \
    check_webdav, \
    scan_useful_paths, \
    bruteforce_default_credentials

default_tasks = [
    get_version,
    check_default_error_page,
    check_webdav,
    scan_useful_paths,
    bruteforce_default_credentials
]