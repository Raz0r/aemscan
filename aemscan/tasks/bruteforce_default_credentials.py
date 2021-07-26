__author__ = 'raz0r'

import os
import click
import string
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def run(url):
    response = requests.get(url + '/', auth=('baseline', 'request'), verify=False)
    if response.status_code != 401:

        click.echo(click.style('AEM authentication is not available', fg='red'))
        return

    click.echo(click.style('AEM authentication is available', fg='green'))
    with open(os.path.dirname(__file__) + '/../data/aem-default-creds.txt', 'r') as f:
        creds = list(map(str.strip, f.readlines()))
        found = []
        with click.progressbar(creds, label='Checking default credentials') as bar:
            for line in bar:
                (login, password) = line.split(':')
                response = requests.post(url + '/', auth=(login, password), verify=False)
                if response.status_code == 200:
                    found.append(line)
    if found:
        click.echo(click.style('Found {} default credentials!'.format(len(found)), fg='green'))
        for item in found:
            click.echo(click.style('{}'.format(item), fg='green'))
