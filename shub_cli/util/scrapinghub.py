from shub.config import load_shub_config


def get_sh_api_key(api):
    """
    Return a valid API key either by returning the api passed as parameter or finding the default API KEY in
    .scrapinghub.yml file

    :param api: An api key
    :return: Api key
    """
    if api is not None:
        return api
    else:
        config = load_shub_config()
        try:
            return config.apikeys['default']
        except KeyError:
            return None


def get_sh_project(project):
    """
    Return a valid project id either by returning the id passed as parameter or finding the default PROJECT ID in
    .scrapinghub.yml file

    :param project: A project id
    :return: Project id
    """
    if project is not None:
        return project
    else:
        config = load_shub_config()
        try:
            return config.projects['default']
        except KeyError:
            return None
