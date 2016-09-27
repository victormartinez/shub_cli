from shub_cli.util.parse import get_job_main_info
from terminaltables import SingleTable

TABLE_JOB_MODEL = [
    ['Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']
]

TABLE_JOBS_MODEL = [
    ['Id', 'Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']
]


def display(job, click):
    main_info = get_job_main_info(job)
    table_data = TABLE_JOB_MODEL.copy()
    table_data.append(
        [main_info['spider'], main_info['started_time'], main_info['items_scraped'], main_info['tags'],
         main_info['state'], main_info['close_reason'], main_info['errors_count'], main_info['version']]
    )
    table = SingleTable(table_data)
    click.echo(table.table)


def display_jobs(jobs, click):
    table_data = TABLE_JOBS_MODEL.copy()
    for job in jobs:
        main_info = get_job_main_info(job)
        table_data.append(
            [main_info['id'], main_info['spider'], main_info['started_time'], main_info['items_scraped'],
             main_info['tags'], main_info['state'], main_info['close_reason'], main_info['errors_count'],
             main_info['version']]
        )
    table = SingleTable(table_data)
    click.echo(table.table)
