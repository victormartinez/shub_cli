from toolz import dicttoolz


def parse_options(tag, lacks, spider, state):
    params = dict(
        lacks_tag=lacks,
        has_tag=tag,
        spider=spider,
        state=state
    )
    return dicttoolz.valfilter(lambda v: v is not None, params)


def parse_list_to_string(tags):
    if len(tags) == 1:
        return tags[0]
    return ', '.join(tags)


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
        tags = parse_list_to_string(info['tags'])

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
