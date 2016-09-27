def display(job):
    if job:
        info = job.info
        print('')
        print('##############################')
        print('Job: {}'.format(info['id']))
        print('##############################')
        if 'started_time' in info.keys():
            print('Started At: {}'.format(info['started_time']))

        print('Spider: {}'.format(info['spider']))
        print('Items Scraped: {}'.format(info['items_scraped']))
        print('State: {}'.format(info['state']))

        if 'close_reason' in info.keys():
            print('Close Reason: {}'.format(info['close_reason']))

        print('Errors: {}'.format(info['errors_count']))
        print('Spider Args: {}'.format(info['spider_args']))
        print('Tags: {}'.format(info['tags']))
        print('Version: {}'.format(info['version']))
    else:
        print('')
        print('Job not found')


def display_jobs(jobs):
    if not jobs:
        print('Jobs not found')

    for job in jobs:
        display(job)
