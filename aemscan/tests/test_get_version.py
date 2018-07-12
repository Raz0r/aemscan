__author__ = 'raz0r'

from ..tasks import get_version


def test_get_version():
    with open('.feed.xml', 'r') as f:
        assert get_version.parse_response(f.read()) == '6.0'