__author__ = 'raz0r'

import click
import requests
import xml.etree.ElementTree as ET


def run(url):
    response = requests.get(url + '/.feed')
    version = parse_response(response.content)
    if version:
        click.echo(click.style('AEM version: {}'.format(version), fg='green'))
    else:
        click.echo(click.style('Cannot get AEM version', fg='red'))


def parse_response(response):
    try:
        xml = ET.fromstring(response)
    except (ValueError, ET.ParseError):
        return False
    for node in xml:
        if node.tag.endswith('generator') and node.attrib.get('version'):
            return node.attrib.get('version')
    return False