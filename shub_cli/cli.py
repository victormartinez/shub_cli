import click
from click_repl import register_repl
from scrapinghub import Connection
from shub_cli.commands.job import get_job, get_jobs
from shub_cli.util.display import display, display_jobs
from shub_cli.util.parse import create_dict
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


@main.command()
@click.option('--id', type=click.STRING, help='Job Id')
def job(id):
    conn = Connection(apikey=API_KEY)
    job = get_job(id, conn, PROJECT)
    display(job)


@main.command()
@click.option('-tags', nargs=1, type=click.STRING, help='Tags that the jobs must contain separated by comma.')
@click.option('-lacks', nargs=1, type=click.STRING, help='Tags that the jobs can not contain separated by comma.')
@click.option('-spider', nargs=1, type=click.STRING, help='Name of the spider.')
@click.option('-state', nargs=1, type=click.STRING, help='State of the job.')
@click.option('-count', nargs=1, type=click.INT, help='Number of results.', default=10)
def jobs(tags, lacks, spider, state, count):
    options = create_dict(tags, lacks, spider, state, count)
    conn = Connection(apikey=API_KEY)
    jobs = get_jobs(options, conn, PROJECT)
    display_jobs(jobs)


register_repl(main)
