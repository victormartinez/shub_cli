# -*- coding: utf-8 -*-


def get_job(id, conn, project):
    return conn[project].job(id)


def get_jobs(params, conn, project, count):
    return conn[project].jobs(**params, count=count)
