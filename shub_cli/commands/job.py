# -*- coding: utf-8 -*-
from scrapinghub import Connection


class Job(object):
    """Job"""

    def __init__(self, options, **kwargs):
        print(options)
        self.job_id = options['-id']
        self.conn = Connection(apikey=kwargs['api_key'])
        self.project = kwargs['project']

    def run(self):
        return self.conn[self.project].job(self.job_id)
