"""
Scrapinghub CLI

Usage:
  shub-cli jobs
  shub-cli jobs [-t TAG1,TAG2] [-l LACK1,LACK2] [-s SPIDER] [-e STATE] [-c COUNT]
  shub-cli job -id <id>

Options:
  -t TAG1,TAG2    Tags that the jobs must contain.
  -l LACK1,LACK2  Tags that the jobs can not contain.
  -s SPIDER       Name of the spider.
  -e STATE        State of the job.
  -c COUNT        Number of results.

Examples:
  shub-cli jobs
  shub-cli jobs -c 100
  shub-cli jobs -t fast,production -l consumed,dev -s spider1 state finished
  shub-cli job -id '10/10/1000'


Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/victormartinez/shub_cli
"""
import click
from scrapinghub import Connection
from shub.config import load_shub_config
from shub_cli.commands.job import get_job, get_jobs
from shub_cli.util.display import display, display_jobs
from shub_cli.util.parse import create_dict

config = load_shub_config()
api_keys = config.apikeys
projects = config.projects

default_api_key = api_keys['default']
default_project = projects['default']

conn = Connection(apikey=default_api_key)


@click.group()
def main():
    """Main CLI entrypoint."""
    pass


@click.command()
@click.option('--id', type=click.STRING, help='Job Id')
def job(id):
    job = get_job(id, conn, default_project)
    display(job)


@click.command()
@click.option('-tags', nargs=1, type=click.STRING, help='Tags that the jobs must contain.')
@click.option('-lacks', nargs=1, type=click.STRING, help='Tags that the jobs can not contain.')
@click.option('-spider', nargs=1, type=click.STRING, help='Name of the spider.')
@click.option('-state', nargs=1, type=click.STRING, help='State of the job.')
@click.option('-count', nargs=1, type=click.INT, help='Number of results.', default=10)
def jobs(tags, lacks, spider, state, count):
    # shub-cli jobs -tags a,b,c -lacks a -state state
    options = create_dict(tags, lacks, spider, state, count)
    jobs = get_jobs(options, conn, default_project)
    display_jobs(jobs)


main.add_command(job)
main.add_command(jobs)
