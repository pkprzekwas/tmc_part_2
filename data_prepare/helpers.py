import os
import glob

import pandas as pd

from consts import DATA_DIR, LAST_CORRECT_DATE


def extract_date(path):
    _ = path.split('/')[-1]
    _ = _.split('.')[0]
    _ = _.split('_')[2]
    return _


def get_correct_dates(date):
    if int(date) > int(LAST_CORRECT_DATE):
        return date


def get_all_days():
    scheme = '*.npy'
    files = glob.glob(os.path.join(DATA_DIR, scheme))
    dates = map(extract_date, files)
    filtered_dates = filter(get_correct_dates, dates)
    return filtered_dates


def matrix_to_csv(m, path):
    frame = pd.DataFrame(data=m[1:, 1:],
                         index=m[1:, 0],
                         columns=m[0, 1:])
    frame.to_csv(path_or_buf=path)
