__author__ = 'raz0r'

import os
import click
import string
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def run(url):
    with open(os.path.dirname(__file__) + '/../data/aem-paths.txt', 'r') as f:
        paths = list(map(str.strip, f.readlines()))
        found = []
        with click.progressbar(paths, label='Scanning useful paths') as bar:
            for path in bar:
                try:
                    response = requests.head(url + path, timeout=40, verify=False)
                    if response.status_code == 200:
                        found.append(path)
                except:
                    error('\nException while performing a check for {}'.format(url + path))

    if found:
        click.echo(click.style('Found {} paths:'.format(len(found)), fg='green'))
        for item in found:
            click.echo(click.style('{}'.format(item), fg='green'))


def error(message):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    click.echo(click.style(message, fg='red'))
    click.echo(click.style('Exception type: {}'.format(str(exc_type)), fg='red'))
    click.echo(click.style('Exception value: {}'.format(str(exc_value)), fg='red'))
