__author__ = 'raz0r'
__version__ = '1.0'

import click

from .tasks import default_tasks
from .types import URL

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('url', type=URL())
@click.version_option()
def main(url):
    """\b
           ______ __  __  _____
     /\   |  ____|  \/  |/ ____|
    /  \  | |__  | \  / | (___   ___ __ _ _ __
   / /\ \ |  __| | |\/| |\___ \ / __/ _` | '_ \\
  / ____ \| |____| |  | |____) | (_| (_| | | | |
 /_/    \_\______|_|  |_|_____/ \___\__,_|_| |_|


aemscan - Adobe Experience Manager Vulnerability Scanner"""

    click.echo(main.__doc__)
    click.echo("version: {}\n".format(__version__))

    for task in default_tasks:
        task.run(url)

if __name__ == '__main__':
    main()