from shub_cli.config.display import TABLE_JOB_MODEL, TABLE_JOBS_MODEL
from shub_cli.util.parse import get_job_main_info
from terminaltables import SingleTable


def display(job, click):
    """
    Display the job information.

    :param job: A Job object provided by ScrapingHub
    :param click: A click object used to print on the terminal
    """
    if job:
        main_info = get_job_main_info(job)
        table_data = list(TABLE_JOB_MODEL)
        table_data.append(
            [main_info['spider'], main_info['started_time'], main_info['items_scraped'], main_info['tags'],
             main_info['state'], main_info['close_reason'], main_info['errors_count'], main_info['version']]
        )
        table = SingleTable(table_data)
        click.echo(table.table)


def display_jobs(jobs, click):
    """
    Display all the jobs' information contained in a JobSet.

    :param jobs: A JobSet object provided by ScrapingHub with all the jobs
    :param click: A click object used to print on the terminal
    """
    table_data = list(TABLE_JOBS_MODEL)
    for job in jobs:
        main_info = get_job_main_info(job)
        table_data.append(
            [main_info['id'], main_info['spider'], main_info['started_time'], main_info['items_scraped'],
             main_info['tags'], main_info['state'], main_info['close_reason'], main_info['errors_count'],
             main_info['version']]
        )
    table = SingleTable(table_data)
    click.echo(table.table)


def display_log(job, click):
    """
    Display all log messages.

    :param job: A Job object provided by ScrapingHub
    :param click: A click object used to print on the terminal
    :return:
    """
    logs = job.log()

    for log in logs:
        click.echo(log + '\n')
