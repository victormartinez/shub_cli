import pytest
from mock import patch
from shub_cli.commands.spider import get_spiders


@pytest.fixture
def spiders():
    return [
        {
            'id': 'spider1',
            'tags': [],
            'version': '1.0.20161005142056',
            'type': 'manual'
        },
        {
            'id': 'spider2',
            'tags': [],
            'version': '1.0.20161005142056',
            'type': 'manual'
        },
    ]


@patch('scrapinghub.Connection')
def test_get_spiders(conn, spiders):
    conn['123456'].spiders.return_value = spiders
    actual_spiders = get_spiders(conn, '128901')
    assert actual_spiders == spiders
