__author__ = 'raz0r'

import os
import click
import string
import requests


def run(url):
    with open(os.path.dirname(__file__) + '/../data/aem-paths.txt', 'r') as f:
        paths = map(string.strip, f.readlines())
        found = []
        with click.progressbar(paths, label='Scanning useful paths') as bar:
            for path in bar:
                response = requests.head(url + path)
                if response.status_code == 200:
                    found.append(path)
    if found:
        click.echo(click.style('Found {} paths:'.format(len(found)), fg='green'))
        for item in found:
            click.echo(click.style('{}'.format(item), fg='green'))