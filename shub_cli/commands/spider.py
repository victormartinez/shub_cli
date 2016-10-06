# -*- coding: utf-8 -*-


def get_spiders(conn, project):
    """
    Get a list of spiders from ScrapingHub.

    :param conn: Valid connection object
    :param project: Project id
    :return: A List of dicts provided by ScrapingHub
    """
    return list(conn[project].spiders())
