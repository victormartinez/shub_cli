from shub.config import load_shub_config


def get_sh_api_key(api):
    if api:
        return api

    config = load_shub_config()
    try:
        return config.apikeys['default']
    except KeyError:
        return None


def get_sh_project(project):
    if project:
        return project

    config = load_shub_config()
    try:
        return config.projects['default']
    except KeyError:
        return None


def get_job_main_info(job):
    info = job.info
    main_info = {}
    main_info.update({'id': job.id})
    main_info.update({'spider': info['spider']})

    state = ''
    if 'state' in info.keys():
        state = info['state']

    items_scraped = ''
    if 'items_scraped' in info.keys():
        items_scraped = info['items_scraped']

    errors_count = ''
    if 'errors_count' in info.keys():
        errors_count = info['errors_count']

    tags = ''
    if 'tags' in info.keys():
        tags = info['tags']

    version = ''
    if 'version' in info.keys():
        version = info['version']

    started = ''
    if 'started_time' in info.keys():
        started = info['started_time']

    close = ''
    if 'close_reason' in info.keys():
        close = info['close_reason']

    main_info.update({'state': state})
    main_info.update({'items_scraped': items_scraped})
    main_info.update({'errors_count': errors_count})
    main_info.update({'tags': tags})
    main_info.update({'version': version})
    main_info.update({'started_time': started})
    main_info.update({'close_reason': close})
    return main_info

