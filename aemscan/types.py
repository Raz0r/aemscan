__author__ = 'raz0r'

import click
try:
    from urlparse import urlparse
except (ImportError, ModuleNotFoundError):
    from urllib.parse import urlparse


class URL(click.ParamType):
    name = 'url'

    def convert(self, value, param, ctx):
        if not isinstance(value, tuple):
            value = urlparse(value)
            if value.scheme not in ('http', 'https'):
                self.fail('invalid URL scheme (%s).  Only HTTP URLs are '
                          'allowed' % value.scheme, param, ctx)
        return value.scheme + '://' + value.netloc
