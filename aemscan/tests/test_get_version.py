__author__ = 'raz0r'

import os
from ..tasks import get_version


def test_get_version():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    with open(path + '.feed.xml', 'r') as f:
        assert get_version.parse_response(f.read()) == '6.0'
