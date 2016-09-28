import pytest
from mock import patch
from scrapinghub import Job
from shub_cli.commands.job import get_jobs, get_job


@pytest.fixture
def job():
    return Job(
        project='128901',
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
def params():
    return {'has_tag': 'production', 'lacks_tag': 'development', 'spider': 'my-spider'}


@patch('scrapinghub.Connection')
def test_get_jobs(conn, job, params):
    conn['123456'].jobs.return_value = [job]
    jobs = get_jobs(params, conn, '128901')
    assert jobs == [job]


@patch('scrapinghub.Connection')
def test_get_job(conn, job):
    conn['123456'].job.return_value = job
    actual = get_job('63796/5/2', conn, '128901')
    assert actual == job
