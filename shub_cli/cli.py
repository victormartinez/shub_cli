import click
import requests
import scrapinghub
from click_repl import register_repl
from prompt_toolkit.shortcuts import print_tokens
from scrapinghub import Connection

from shub_cli.commands.job import get_job, get_jobs
from shub_cli.config.display import shub_not_configured_tokens, error_style, no_internet_connection_tokens, \
    shub_api_error_tokens
from shub_cli.config.shub_config import config
from shub_cli.util.display import display, display_jobs, display_log
from shub_cli.util.parse import parse_options
from shub_cli.util.scrapinghub import get_sh_api_key, get_sh_project


@click.group()
@click.option('-api', nargs=1, type=click.STRING, help='ScrapingHub API KEY', default=config.api_key)
@click.option('-project', nargs=1, type=click.STRING, help='Scrapinghub Project Id', default=config.project_id)
def main(api, project):
    """Main CLI Entrypoint"""
    if config.api_key is None and config.project_id is None:
        API_KEY = get_sh_api_key(api)
        PROJECT_ID = get_sh_project(project)

        config.api_key = API_KEY
        config.project_id = PROJECT_ID

    if config.api_key is None and config.project_id is None:
        print_tokens(shub_not_configured_tokens, style=error_style)
        exit()


@main.command()
@click.option('-id', type=click.STRING, help='Job Id')
@click.option('--with-log', is_flag=True, help='Presents the log of a job')
def job(id, with_log):
    """See information of a job"""
    conn = Connection(apikey=config.api_key)
    try:
        job = get_job(id, conn, config.project_id)
        display(job, click)
        if with_log:
            display_log(job, click)
    except requests.exceptions.ConnectionError:
        print_tokens(no_internet_connection_tokens, style=error_style)
    except scrapinghub.APIError:
        print_tokens(shub_api_error_tokens, style=error_style)


@main.command()
@click.option('-tag', nargs=1, type=click.STRING, help='Tag that the jobs must contain.')
@click.option('-lacks', nargs=1, type=click.STRING, help='Tag that the jobs can not contain.')
@click.option('-spider', nargs=1, type=click.STRING, help='Name of the spider.')
@click.option('-state', nargs=1, type=click.STRING, help='State of the job.')
@click.option('-count', nargs=1, type=click.INT, help='Quantity of results.', default=10)
def jobs(tag, lacks, spider, state, count):
    """See information of N jobs"""
    params = parse_options(tag, lacks, spider, state, count)
    conn = Connection(apikey=config.api_key)
    try:
        jobs = get_jobs(params, conn, config.project_id)
        display_jobs(jobs, click)
    except requests.exceptions.ConnectionError:
        print_tokens(no_internet_connection_tokens, style=error_style)
    except scrapinghub.APIError:
        print_tokens(shub_api_error_tokens, style=error_style)


register_repl(main)
