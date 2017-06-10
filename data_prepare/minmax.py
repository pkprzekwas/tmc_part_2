import os

import numpy as np

import data_prepare.consts as consts
from data_prepare.matrix_getter import get_mat_day, get_mat_month
from data_prepare.helpers import get_all_days, matrix_to_csv


def max_days():
    calc_day(np.maximum, consts.MAX_DAY_DIR)


def min_days():
    calc_day(np.minimum, consts.MIN_DAY_DIR)


def calc_day(func, out_path):
    days_to_cnt = get_all_days()

    for day in days_to_cnt:
        files_to_cnt = get_mat_day(day)
        val = files_to_cnt[0]

        for mat in files_to_cnt[1:]:
            val = func(val, mat)

        path = os.path.join(out_path, '%s.csv' % day)
        matrix_to_csv(val, path)


def max_mth():
    calculate(np.maximum, consts.MAX_MONTHS_DIR, scope='months')


def min_mth():
    calculate(np.minimum, consts.MIN_MONTHS_DIR, scope='months')


def max_yr():
    calculate(np.maximum, consts.MAX_YEARS_DIR, scope='years')


def min_yr():
    calculate(np.minimum, consts.MIN_YEARS_DIR, scope='years')


def calculate(func, out_path, scope='months'):
    year_val = None

    if func == np.maximum:
        year_val = np.zeros(shape=consts.ARRAY_SIZE)

    if func == np.minimum:
        year_val = np.full(shape=consts.ARRAY_SIZE, fill_value=np.inf)

    if not hasattr(func, '__call__'):
        raise ValueError('func object should be a function.')

    for mth in consts.MONTHS:
        matrices = get_mat_month(mth)

        val = matrices[0]

        for mat in matrices[1:]:
            val = func(val, mat)

        if scope == 'months':
            path = os.path.join(out_path, '%s.csv' % mth)
            matrix_to_csv(val, path)

        if scope == 'years':
            year_val = func(year_val, val)

    if scope == 'years':
        path = os.path.join(out_path, consts.YR_FILE)
        matrix_to_csv(year_val, path)
