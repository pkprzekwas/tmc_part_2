import os

import numpy as np
import pandas as pd

import consts
from matrix_getter import get_mat_month


def cnt_avg(mode='months'):
    year_sum = np.zeros(shape=consts.ARRAY_SIZE)

    for mth in consts.MONTHS:
        matrices = get_mat_month(mth)
        avg = _sum(matrices) / len(matrices)

        if mode == 'months':
            path = os.path.join(consts.AVG_MONTHS_DIR, '%s.csv' % mth)
            frame = pd.DataFrame(data=avg[1:, 1:],
                                 index=avg[1:, 0],
                                 columns=avg[0, 1:])
            frame.to_csv(path_or_buf=path)

        elif mode == 'years':
            year_sum += avg

    if mode == 'years':
        avg = year_sum / len(consts.MONTHS)
        path = os.path.join(consts.AVG_YEARS_DIR, consts.YR_FILE)
        frame = pd.DataFrame(data=avg[1:, 1:],
                             index=avg[1:, 0],
                             columns=avg[0, 1:])
        frame.to_csv(path_or_buf=path)


def _sum(matrices):
    sum_ = np.zeros(shape=consts.ARRAY_SIZE)
    for mat in matrices:
        sum_ += mat
    return sum_
