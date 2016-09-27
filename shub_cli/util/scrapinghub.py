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
