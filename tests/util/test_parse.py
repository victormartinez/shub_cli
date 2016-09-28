import pytest
from scrapinghub import Job
from shub_cli.util.parse import get_job_main_info, parse_list_to_string, parse_options


@pytest.fixture
def job1():
    return Job(
        project='',
        id='63796/5/2',
        info={
            u'close_reason': u'finished',
            u'elapsed': 3567293218,
            u'errors_count': 0,
            u'id': u'63796/5/2',
            u'items_scraped': 496,
            u'logs': 34,
            u'priority': 2,
            u'responses_received': 501,
            u'spider': u'my-spider',
            u'spider_type': u'manual',
            u'started_time': u'2016-05-31T16:46:46',
            u'state': u'finished',
            u'tags': [u'production'],
            u'updated_time': u'2016-05-31T16:59:28',
            u'version': u'1.0.20160531165928'
        }
    )


@pytest.fixture
def job2():
    return Job(
        project='',
        id='63796/5/3',
        info={
            u'id': u'63796/5/2',
            u'logs': 0,
            u'priority': 2,
            u'spider': u'my-spider',
            u'spider_type': u'manual',
            u'state': u'pending',
            u'tags': [u'production'],
        }
    )


def test_get_job_main_info(job1):
    main_info = get_job_main_info(job1)
    assert main_info == {'close_reason': 'finished',
                         'errors_count': 0,
                         'id': '63796/5/2',
                         'items_scraped': 496,
                         'spider': 'my-spider',
                         'started_time': '2016-05-31T16:46:46',
                         'state': 'finished',
                         'tags': 'production',
                         'version': '1.0.20160531165928'}


def test_get_job_main_info_with_less_information(job2):
    main_info = get_job_main_info(job2)
    assert main_info == {'spider': 'my-spider',
                         'started_time': '',
                         'close_reason': '',
                         'state': 'pending',
                         'version': '',
                         'items_scraped': '',
                         'id': '63796/5/3',
                         'tags': 'production',
                         'errors_count': ''}


@pytest.mark.parametrize("tag_list,expected", [
    (['production', 'normal'], 'production, normal'),
    (['production'], 'production'),
    ([], ''),
])
def test_parse_list_to_string(tag_list, expected):
    tags_string = parse_list_to_string(tag_list)
    assert tags_string == expected


@pytest.mark.parametrize("tag, lacks, spider, state, count, expected", [
    ('production', None, None, None, None, {'has_tag': 'production', 'count': 10}),
    ('production', 'development', None, None, None, {'has_tag': 'production', 'lacks_tag': 'development', 'count': 10}),
    ('production', 'development', 'my-spider', None, None, {'has_tag': 'production', 'lacks_tag': 'development', 'spider': 'my-spider', 'count': 10}),
    ('production', 'development', 'my-spider', 'finished', None, {'has_tag': 'production', 'lacks_tag': 'development', 'spider': 'my-spider', 'state': 'finished', 'count': 10}),
    ('production', 'development', 'my-spider', 'finished', 30, {'has_tag': 'production', 'lacks_tag': 'development', 'spider': 'my-spider', 'state': 'finished', 'count': 30}),
    (None, None, None, None, 30, {'count': 30}),
    (None, None, None, 'finished', 30, {'state': 'finished', 'count': 30}),
    (None, None, 'my-spider', 'finished', 30, {'state': 'finished', 'count': 30, 'spider': 'my-spider'}),
    (None, 'development', 'my-spider', 'finished', 30, {'state': 'finished', 'lacks_tag': 'development', 'count': 30, 'spider': 'my-spider'}),
])
def test_parse_options(tag, lacks, spider, state, count, expected):
    options = parse_options(tag, lacks, spider, state, count)
    print(options)
    assert options == expected
