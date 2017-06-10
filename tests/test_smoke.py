import subprocess

import pytest

from data_prepare import consts, matrix_getter, helpers, main
from tests.helpers import gen_days


@pytest.mark.slow
def test_main():
    main.main()
    generated_files = subprocess.check_output(
        ['./cnt_output.sh', consts.OUT_DIR], cwd=consts.TEST_DIR)
    assert int(generated_files) == 39
    subprocess.call(['./clean_csv.sh'], cwd=consts.PROJECT_DIR)
    generated_files = subprocess.check_output(
        ['./cnt_output.sh', consts.OUT_DIR], cwd=consts.TEST_DIR)
    assert int(generated_files) == 0


def test_read_matrix(wind_matrix):
    assert wind_matrix.shape == (361, 720)


def test_gen_days():
    days = gen_days('2017', '04', 30)
    assert days[0] == '20170401'
    assert days[15] == '20170416'
    assert days[29] == '20170430'


def test_get_first_of_april(wind_matrices_for_april_first):
    assert len(wind_matrices_for_april_first) == consts.NUM_OF_DATA_FOR_A_DAY


def test_get_april(wind_matrices_for_april):
    assert len(wind_matrices_for_april) == consts.NUM_OF_DATA_FOR_APRIL


def test_days_in_april():
    days = gen_days('2017', '04', 30)
    matrices_for_day = map(matrix_getter.get_mat_day, days)
    matrices = []
    for day in matrices_for_day:
        matrices.extend(day)
    assert len(matrices) == consts.NUM_OF_DATA_FOR_APRIL


def test_year_data():
    matrices = []
    for month in consts.MONTHS:
        matrices_for_month = matrix_getter.get_mat_month(month)
        matrices.extend(matrices_for_month)
    assert len(matrices) == 1255


def test_get_all_dates():
    dates = helpers.get_all_days()
    assert len(dates) == 1255
