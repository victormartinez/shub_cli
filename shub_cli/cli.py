"""
Scrapinghub CLI

Usage:
  shub-cli jobs
  shub-cli jobs [-t TAG1,TAG2] [-l LACK1,LACK2] [-s SPIDER] [-e STATE] [-c COUNT]
  shub-cli job -id <id>

Options:
  -t TAG1,TAG2    Description.
  -l LACK1,LACK2  Description.
  -s SPIDER       Description.
  -e STATE        Description.
  -c COUNT        Description.

Examples:
  shub-cli jobs
  shub-cli jobs -c 100
  shub-cli jobs -t fast,production -l consumed,dev -s spider1 state finished
  shub-cli job -id '10/10/1000'


Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/victormartinez/shub_cli
"""
from docopt import docopt
from shub_cli import __version__ as VERSION
from shub.config import load_shub_config
from shub_cli.commands.job import Job
from shub_cli.commands.jobs import Jobs
from shub_cli.util.display import display, display_jobs

config = load_shub_config()
api_keys = config.apikeys
projects = config.projects


def main():
    """Main CLI entrypoint."""
    default_api_key = api_keys['default']
    default_project = projects['default']
    options = dict(docopt(__doc__, version=VERSION).items())

    print('Connection: {}'.format(default_api_key))
    print('Project: {}'.format(default_project))

    if 'job' in options.keys() and options['job'] == True:
        if '-id' in options.keys():
            job = Job(options, api_key=default_api_key, project=default_project)
            display(job.run())
        else:
            print('')
            print('Wrong command.')

    if 'jobs' in options.keys() and options['jobs'] == True:
        jobs = Jobs(options, api_key=default_api_key, project=default_project)
        display_jobs(jobs.run())
