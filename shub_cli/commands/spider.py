# -*- coding: utf-8 -*-


def get_spiders(conn, project):
    return list(conn[project].spiders())
