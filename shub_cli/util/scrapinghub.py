from shub.config import load_shub_config


def get_sh_api_key(api):
    if api:
        return api

    config = load_shub_config()
    return config.apikeys['default']


def get_sh_project(project):
    if project:
        return project

    config = load_shub_config()
    return config.projects['default']