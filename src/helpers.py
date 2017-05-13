def extract_date(path):
    _ = path.split('/')[-1]
    _ = _.split('.')[0]
    _ = _.split('_')[2]
    return _

