"""
Those matrices below are the border for file format change:
    - 'gfsanl_4_20160511_1200_000.grb2.npy'
    - 'gfsanl_4_20160511_0600_000.grb2.npy'
"""
import os

import pytest

import data_prepare.consts as consts
from data_prepare.matrix_getter import get_mat, get_mat_month


@pytest.fixture(scope='session')
def wind_matrix():
    mat_path = os.path.join(consts.DATA_DIR, consts.TEST_FILE)
    mat = get_mat(mat_path)
    return mat


@pytest.fixture(scope='session')
def wind_matrices_for_april():
    """Wind speed matrices for April 2017."""
    mat = get_mat_month(201704)
    return mat


@pytest.fixture(scope='session')
def wind_matrices_for_april_first():
    """Wind speed matrices for April 2017."""
    mat = get_mat_month(20170401)
    return mat
