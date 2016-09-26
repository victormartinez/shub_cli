# -*- coding: utf-8 -*-
from scrapinghub import Connection


class Jobs(object):
    """Jobs"""

    def __init__(self, options, **kwargs):
        self.count = options['-c'] or 10
        self.has_tags = self._split_values(options['-t'])
        self.state = options['-e']
        self.spider = options['-s']
        self.lacks_tags = self._split_values(options['-l'])
        self.conn = Connection(apikey=kwargs['api_key'])
        self.project = kwargs['project']

    def _split_values(self, values):
        if not values:
            return None
        return values.split(',')

    def run(self):
        return self._jobs()

    def _jobs(self):
        params = self._get_params()
        project = self.conn[self.project]
        return project.jobs(**params, count=self.count)

    def _get_params(self):
        params = {}
        if self.spider:
            params.update({'spider': self.spider})

        if self.state:
            params.update({'state': self.state})

        if self.has_tags:
            params.update({'has_tag': self.has_tags})

        if self.lacks_tags:
            params.update({'lacks_tag': self.lacks_tags})

        return params
