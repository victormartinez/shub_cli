# -*- coding: utf-8 -*-

def get_jobs_with_error(project, count=10):
    jobs_with_error = []
    start = 0

    while len(jobs_with_error) < count:
        quantity = (count * 10)
        jobs = project.jobq.list(start=start, state='finished', count=quantity)
        jobs_with_error.extend([j for j in jobs if j.get('errors')])
        start += quantity

    return jobs_with_error
