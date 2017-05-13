import os

import numpy as np
import pandas as pd

import consts
from matrix_getter import get_mat_month


def max_mth():
    calculate(np.maximum, consts.MAX_MONTHS_DIR, scope='months')


def min_mth():
    calculate(np.minimum, consts.MIN_MONTHS_DIR, scope='months')


def max_yr():
    calculate(np.maximum, consts.MAX_YEARS_DIR, scope='years')


def min_yr():
    calculate(np.minimum, consts.MIN_YEARS_DIR, scope='years')


def calculate(func, out, scope='months'):
    if func == np.maximum:
        year_val = np.zeros(shape=consts.ARRAY_SIZE)

    if func == np.minimum:
        year_val = np.full(shape=consts.ARRAY_SIZE, fill_value=np.inf)

    if not hasattr(func, '__call__'):
        raise ValueError('func object should be function.')

    for mth in consts.MONTHS:
        matrices = get_mat_month(mth)

        val = matrices[0]

        for mat in matrices[1:]:
            val = func(val, mat)

        if scope == 'months':
            path = os.path.join(out, '%s.csv' % mth)
            frame = pd.DataFrame(data=val[1:, 1:],
                                 index=val[1:, 0],
                                 columns=val[0, 1:])
            frame.to_csv(path_or_buf=path)

        if scope == 'years':
            year_val = func(year_val, val)

    if scope == 'years':
        path = os.path.join(out, consts.YR_FILE)
        frame = pd.DataFrame(data=year_val[1:, 1:],
                             index=year_val[1:, 0],
                             columns=year_val[0, 1:])
        frame.to_csv(path_or_buf=path)
