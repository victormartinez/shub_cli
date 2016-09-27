# -*- coding: utf-8 -*-
from shub_cli.util.parse import parse_options


def get_job(id, conn, project):
    return conn[project].job(id)


def get_jobs(options, conn, project):
    params = parse_options(options)
    return conn[project].jobs(**params, count=options['count'])
