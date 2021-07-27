__author__ = 'raz0r'

import click
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def run(url):
    response = requests.options(url + '/', verify=False)
    if 'propfind' in response.headers.get('allow', '').lower() or response.status_code == 401:
        click.echo(click.style('WebDAV is enabled', fg='green'))
    else:
        click.echo(click.style('WebDAV is disabled', fg='red'))
