import mock
from shub.config import ShubConfig
from shub_cli.util.scrapinghub import get_sh_api_key, get_sh_project


def load_shub_config():
    config = ShubConfig()
    config.apikeys = {'default': '1q2w3e4r5t6y7u'}
    config.projects = {'default': '19876'}
    return config


def load_non_default_shub_config():
    config = ShubConfig()
    config.apikeys = {'production': '3e4rq5tw6y17u'}
    config.projects = {'production': '98012'}
    return config


def test_get_sh_api_key_in_scrapinghub_file():
    with mock.patch('shub_cli.util.scrapinghub.load_shub_config', side_effect=load_shub_config):
        api = get_sh_api_key(None)
        assert api == '1q2w3e4r5t6y7u'


def test_get_sh_project_in_scrapinghub_file():
    with mock.patch('shub_cli.util.scrapinghub.load_shub_config', side_effect=load_shub_config):
        api = get_sh_project(None)
        assert api == '19876'


def test_get_sh_non_default_api_key_in_scrapinghub_file():
    with mock.patch('shub_cli.util.scrapinghub.load_shub_config', side_effect=load_non_default_shub_config):
        api = get_sh_api_key(None)
        assert api == None


def test_get_sh_non_default_project_in_scrapinghub_file():
    with mock.patch('shub_cli.util.scrapinghub.load_shub_config', side_effect=load_non_default_shub_config):
        api = get_sh_project(None)
        assert api == None


def test_get_sh_api_key():
    api_key = get_sh_api_key('1q2w3e4r5t6y')
    assert api_key == '1q2w3e4r5t6y'


def test_get_sh_project():
    project = get_sh_project('19876')
    assert project == '19876'
