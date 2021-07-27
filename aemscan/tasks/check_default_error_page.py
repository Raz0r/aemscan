__author__ = 'raz0r'

import re
import click
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def run(url):
    response = requests.get(url + '/non_existing', verify=False)
    banner = parse_response(response.content)
    if banner:
        click.echo(click.style('Custom error pages are not enabled, service banner: {}'.format(banner), fg='green'))
    else:
        click.echo(click.style('Custom error pages are enabled', fg='red'))


def parse_response(response):
    match = re.search("<address>(.+?)</address>", response.decode('utf-8'))
    if match:
        return match.group(1)
    return False
