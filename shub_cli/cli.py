import click
import requests
import scrapinghub
from click_repl import register_repl
from prompt_toolkit.shortcuts import print_tokens
from scrapinghub import Connection, HubstorageClient
from shub_cli.commands.job import get_job, get_jobs, get_jobs_with_error
from shub_cli.commands.schedule import schedule_job
from shub_cli.commands.spider import get_spiders
from shub_cli.config.display import shub_not_configured_tokens, error_style, no_internet_connection_tokens, \
    shub_api_error_tokens
from shub_cli.config.shub_config import config
from shub_cli.util.display import display, display_jobs, display_log, display_spiders, display_hc_jobs
from shub_cli.util.parse import parse_options, parse_schedule_options
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
@click.option('-state', nargs=1, type=click.Choice(['pending', 'running', 'finished', 'deleted']),
              help='State of the job.')
@click.option('-count', nargs=1, type=click.INT, help='Quantity of results.', default=10)
@click.option('--with-error', is_flag=True, help='Presents the jobs that contains error')
def jobs(tag, lacks, spider, state, count, with_error):
    """See information of N jobs"""
    try:
        if not with_error:
            conn = Connection(apikey=config.api_key)
            params = parse_options(tag, lacks, spider, state, count)
            jobs = get_jobs(params, conn, config.project_id)
            display_jobs(jobs, click)
        else:
            hc = HubstorageClient(auth=config.api_key)
            project = hc.get_project(config.project_id)
            jobs = get_jobs_with_error(project, count)
            display_hc_jobs(jobs, click)
    except requests.exceptions.ConnectionError:
        print_tokens(no_internet_connection_tokens, style=error_style)
    except scrapinghub.APIError:
        print_tokens(shub_api_error_tokens, style=error_style)


@main.command()
def spiders():
    """List all spiders"""
    conn = Connection(apikey=config.api_key)
    try:
        spiders = get_spiders(conn, config.project_id)
        display_spiders(spiders, click)
    except requests.exceptions.ConnectionError:
        print_tokens(no_internet_connection_tokens, style=error_style)
    except scrapinghub.APIError:
        print_tokens(shub_api_error_tokens, style=error_style)


@main.command()
@click.option('-spider', nargs=1, type=click.STRING, help='Spider id')
@click.option('-add-tags', type=click.STRING, multiple=True, help='Add one or more tags to the job')
@click.option('-priority', type=click.IntRange(0, 4), help='Set the priority the job')
def schedule(spider, add_tag, priority):
    """Schedule a job"""
    conn = Connection(apikey=config.api_key)
    params = parse_schedule_options(spider, add_tag, priority)
    try:
        id = schedule_job(conn, config.project_id, params)
        click.echo('Job {} scheduled.\n'.format(id))
    except requests.exceptions.ConnectionError:
        print_tokens(no_internet_connection_tokens, style=error_style)
    except scrapinghub.APIError as exc:
        click.echo("It was not possible to schedule the job. \n{}\n".format(exc))


@main.command()
def config():
    """Check your credentials"""
    text = '''ApiKey: {}\nProject: {}\n'''.format(config.api_key, config.project_id)
    click.echo(text)


register_repl(main)
