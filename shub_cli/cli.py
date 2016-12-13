import click
from click_repl import register_repl
from prompt_toolkit.shortcuts import print_tokens
from scrapinghub import Connection, HubstorageClient
from shub_cli.util.scrapinghub import get_jobs_with_error
from shub_cli.config.display import token_style, create_error_token, create_info_token
from shub_cli.config.shub_config import config
from shub_cli.exceptions import JobNotFound
from shub_cli.util.display import display, display_jobs, display_log, display_spiders, display_hc_jobs
from shub_cli.util.parse import parse_options, parse_schedule_options
from shub_cli.util.scrapinghub import get_sh_api_key, get_sh_project


@click.group()
@click.option('-api', nargs=1, type=click.STRING, help='ScrapingHub API KEY', default=config.api_key)
@click.option('-project', nargs=1, type=click.STRING, help='Scrapinghub Project Id', default=config.project_id)
def main(api, project):
    """Main CLI Entrypoint"""
    if config.api_key is None and config.project_id is None:
        config.api_key = get_sh_api_key(api)
        config.project_id = get_sh_project(project)

    if (config.api_key is None or not len(config.api_key)) and (config.project_id is None or len(config.project_id)):
        message1 = 'You need to set up your .scrapinghub.yml with a default project and api key:\n'
        message2 = '''
         ~/.scrapinghub.yml

         apikeys:
           default: v65a787a987k08k9s797d7s8l98298sw
         projects:
           default: 89090
         \n
         '''

        error_taken = [create_error_token(message1), create_error_token(message2)]
        print_tokens(error_taken, style=token_style)
        exit()


@main.command()
@click.option('-show', nargs=1, type=click.STRING, help='Show a job')
@click.option('-delete', nargs=1, type=click.STRING, help='Delete a job')
@click.option('-cancel', nargs=1, type=click.STRING, help='Cancel a job')
@click.option('--with-log', is_flag=True, help='Display the log of a job')
def job(show, delete, cancel, with_log):
    """See information of a job"""
    options = [show, delete, cancel]
    try:
        if options.count(None) != 2:
            raise ValueError('Wrong command. Please select one of the available options [-show, -delete, -cancel].')

        job_id = next(opt for opt in options if opt is not None)
        conn = Connection(apikey=config.api_key)
        job = conn[config.project_id].job(job_id)
        if job is None:
            raise JobNotFound('Job {} not found.\n'.format(job.id))

        if show:
            display(job, click)
            if with_log:
                display_log(job, click)

        if delete:
            count = job.delete()
            message = 'Deleted {} job with id {}'.format(count, job.id)
            info_tokens = [create_info_token(message)]
            print_tokens(info_tokens, style=token_style)

        if cancel:
            hc = HubstorageClient(auth=config.api_key)
            job = hc.get_job(job_id)
            job.request_cancel()
            message = 'Job cancelled with id {}. You may have to wait a few seconds to see the cancelled status.'.format(
                job_id)
            info_tokens = [create_info_token(message)]
            print_tokens(info_tokens, style=token_style)

    except Exception as exc:
        general_tokens = [create_error_token(str(exc))]
        print_tokens(general_tokens, style=token_style)


@main.command()
@click.option('-tag', nargs=1, type=click.STRING, help='Tag that the jobs must contain.')
@click.option('-lacks', nargs=1, type=click.STRING, help='Tag that the jobs can not contain.')
@click.option('-spider', nargs=1, type=click.STRING, help='Name of the spider.')
@click.option('-state', nargs=1, type=click.Choice(['pending', 'running', 'finished', 'deleted']),
              help='State of the job.')
@click.option('-count', nargs=1, type=click.IntRange(1, 1000), help='Quantity of results.', default=10)
@click.option('--with-error', is_flag=True, help='Presents the jobs that contains error')
def jobs(tag, lacks, spider, state, count, with_error):
    """See information of N jobs"""
    try:
        if not with_error:
            conn = Connection(apikey=config.api_key)
            params = parse_options(tag, lacks, spider, state, count)
            jobs = conn[config.project_id].jobs(**params)
            display_jobs(jobs, click)
        else:
            hc = HubstorageClient(auth=config.api_key)
            project = hc.get_project(config.project_id)
            jobs = get_jobs_with_error(project, count)
            display_hc_jobs(jobs, click)
    except Exception as exc:
        error_taken = [create_error_token(str(exc))]
        print_tokens(error_taken, style=token_style)


@main.command()
def spiders():
    """List all spiders"""
    conn = Connection(apikey=config.api_key)
    try:
        spiders = list(conn[config.project_id].spiders())
        display_spiders(spiders, click)
    except Exception as exc:
        general_tokens = [create_error_token(str(exc))]
        print_tokens(general_tokens, style=token_style)


@main.command()
@click.option('-spider', nargs=1, type=click.STRING, help='Spider id')
@click.option('-tags', nargs=1, type=click.STRING, multiple=True, help='Add one or more tags to the job')
@click.option('-priority', nargs=1, type=click.IntRange(0, 4), help='Set the priority the job')
def schedule(spider, tags, priority):
    """Schedule a job"""
    try:
        if not spider:
            raise ValueError('You must provide an spider name.')

        conn = Connection(apikey=config.api_key)
        params = parse_schedule_options(spider, tags, priority)
        id = conn[config.project_id].schedule(**params)
        info_tokens = [create_info_token('Job {} scheduled with params:\n{}\n'.format(id, params))]
        print_tokens(info_tokens, style=token_style)
    except Exception as exc:
        error_tokens = [create_error_token(str(exc))]
        print_tokens(error_tokens, style=token_style)


@main.command()
def credentials():
    """Check your credentials"""
    info_tokens = [create_info_token('ApiKey: {}\nProject: {}\n'.format(config.api_key, config.project_id))]
    print_tokens(info_tokens, style=token_style)


register_repl(main)
