# -*- coding: utf-8 -*-


def get_job(id, conn, project):
    """
    Get a Job from ScrapingHub.

    :param id: Id of the job
    :param conn: Valid connection object
    :param project: Project id
    :return: A Job object provided by ScrapingHub
    """
    return conn[project].job(id)


def get_jobs(params, conn, project):
    """
    Get a JobSet from ScrapingHub.

    :param params: A dict with the key-values expected by ScrapingHub to search the jobs
    :param conn: Valid connection object
    :param project: Project id
    :param count: The number of results
    :return: A JobSet provided by ScrapingHub
    """
    return conn[project].jobs(**params)
