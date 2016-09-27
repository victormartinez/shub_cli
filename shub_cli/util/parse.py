def parse_options(tag, lacks, spider, state):
    params = {}
    if spider:
        params.update({'spider': spider})

    if state:
        params.update({'state': state})

    if tag:
        params.update({'has_tag': tag})

    if lacks:
        params.update({'lacks_tag': lacks})

    return params
