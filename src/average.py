import os

import numpy as np

import consts
from matrix_getter import get_mat_month, get_mat_day
from helpers import get_all_days, matrix_to_csv


def cnt_avg_per_day():
    days_to_cnt = get_all_days()

    for day in days_to_cnt:
        files_to_cnt = get_mat_day(day)
        sum_ = _sum(files_to_cnt)
        avg = sum_ / len(files_to_cnt)

        path = os.path.join(consts.AVG_DAY_DIR, '%s.csv' % day)
        matrix_to_csv(avg, path)


def cnt_avg(scope='months'):
    year_sum = np.zeros(shape=consts.ARRAY_SIZE)

    for mth in consts.MONTHS:
        matrices = get_mat_month(mth)
        avg = _sum(matrices) / len(matrices)

        if scope == 'months':
            path = os.path.join(consts.AVG_MONTHS_DIR, '%s.csv' % mth)
            matrix_to_csv(avg, path)

        elif scope == 'years':
            year_sum += avg

    if scope == 'years':
        avg = year_sum / len(consts.MONTHS)
        path = os.path.join(consts.AVG_YEARS_DIR, consts.YR_FILE)
        matrix_to_csv(avg, path)


def _sum(matrices):
    sum_ = np.zeros(shape=consts.ARRAY_SIZE)
    for mat in matrices:
        sum_ += mat
    return sum_
