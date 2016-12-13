from toolz import dicttoolz
from datetime import datetime


def parse_options(tag, lacks, spider, state, count):
    """
    Creates a dictionary based on the arguments. Only non-None arguments will be part of the dictionary.

    :param tag: A tag string
    :param lacks: A tag string
    :param spider: A spider string
    :param state: A state string
    :return: A dict with the non-None keys and values
    """
    default_count = 10
    if count:
        default_count = count

    params = dict(
        lacks_tag=lacks,
        has_tag=tag,
        spider=spider,
        state=state,
        count=default_count
    )
    return dicttoolz.valfilter(lambda v: v is not None, params)


def parse_schedule_options(spider, tags, priority):
    params = dict(
        spider=spider,
        add_tag=_get_tags(tags),
        priority=priority
    )
    return dicttoolz.valfilter(lambda v: v is not None, params)


def _get_tags(tags):
    if not tags:
        return None
    return [t.strip() for t in tags[0].split(',') if t != '' and t is not None]


def parse_list_to_string(tags):
    """
    Parses a list of tags into a single string with the tags separated by comma

    :param tags: A list of tags
    :return: A string with tags separated by comma
    """
    return ', '.join(tags)


def get_job_main_info(job):
    """
    Return a dictionary with the pieces of information that will be presented on the terminal.

    :param job: A Job object provided by ScrapingHub
    :return: A dictionary
    """
    info = job.info
    main_info = {
        'id': job.id,
        'spider': info.get('spider'),
        'state': info.get('state', ''),
        'items_scraped': info.get('items_scraped', ''),
        'errors_count': info.get('errors_count', ''),
        'tags': ', '.join(info.get('tags', [])),
        'version': info.get('version', ''),
        'started_time': info.get('started_time', ''),
        'close_reason': info.get('close_reason', ''),
    }
    return main_info


def get_hc_job_main_info(job):
    """
    Return a dictionary with the pieces of information that will be presented on the terminal.
    This method differs from `get_job_main_info` because the object here comes from HubstorageClient and, thus,
    the object has different attributes

    :param job: A Job object provided by ScrapingHub
    :return: A dictionary
    """
    main_info = {
        'id': job.get('key'),
        'spider': job.get('spider'),
        'state': job.get('state', ''),
        'errors_count': job.get('errors', ''),
        'logs': job.get('logs'),
        'version': job.get('version', ''),
        'finished_time': str(datetime.fromtimestamp(job.get('finished_time') / 1000)),
        'close_reason': job.get('close_reason', ''),
    }
    return main_info




