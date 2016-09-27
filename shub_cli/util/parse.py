
def create_dict(tags, lacks, spider, state, count):
    return {
        'tags': tags,
        'lacks': lacks,
        'spider': spider,
        'state': state,
        'count': count
    }


def parse_options(options):
    params = {}
    if options['spider']:
        params.update({'spider': options['spider']})

    if options['state']:
        params.update({'state': options['state']})

    if options['tags']:
        params.update({'has_tag': options['tags'].split(',')})

    if options['lacks']:
        params.update({'lacks_tag': options['lacks'].split(',')})

    return params