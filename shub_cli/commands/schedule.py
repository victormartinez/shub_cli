# -*- coding: utf-8 -*-


def schedule_job(conn, project, params):
    """
    Schedule a job to be run in ScrapingHub server.

    :param conn: Valid connection object
    :param project: Project id
    :return: The unicode job id scheduled
    """
    return conn[project].schedule(**params)
