import click
from click_repl import register_repl
from prompt_toolkit.shortcuts import print_tokens
from scrapinghub import Connection

from shub_cli.commands.job import get_job, get_jobs
from shub_cli.config import error_style, tokens
from shub_cli.util.display import display, display_jobs
from shub_cli.util.parse import parse_options
from shub_cli.util.scrapinghub import get_sh_api_key, get_sh_project

API_KEY = None
PROJECT = None


@click.group()
@click.option('-api', nargs=1, type=click.STRING, help='ScrapingHub API KEY')
@click.option('-project', nargs=1, type=click.STRING, help='Scrapinghub Project Id')
def main(api, project):
    """Main CLI entrypoint."""
    global API_KEY
    global PROJECT
    API_KEY = get_sh_api_key(api)
    PROJECT = get_sh_project(project)
    if API_KEY is None or PROJECT is None:
        print_tokens(tokens, style=error_style)
        exit()


@main.command()
@click.option('-id', type=click.STRING, help='Job Id')
def job(id):
    conn = Connection(apikey=API_KEY)
    job = get_job(id, conn, PROJECT)
    if not job:
        click.echo('Not jobs found.')
    else:
        display(job, click)


@main.command()
@click.option('-tag', nargs=1, type=click.STRING, help='Tag that the jobs must contain.')
@click.option('-lacks', nargs=1, type=click.STRING, help='Tag that the jobs can not contain.')
@click.option('-spider', nargs=1, type=click.STRING, help='Name of the spider.')
@click.option('-state', nargs=1, type=click.STRING, help='State of the job.')
@click.option('-count', nargs=1, type=click.INT, help='Quantity of results.', default=10)
def jobs(tag, lacks, spider, state, count):
    params = parse_options(tag, lacks, spider, state)
    conn = Connection(apikey=API_KEY)
    jobs = get_jobs(params, conn, PROJECT, count)
    display_jobs(jobs, click)


register_repl(main)
