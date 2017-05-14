import glob
import os

import numpy as np

from consts import DATA_DIR, LAST_CORRECT_DATE
from helpers import extract_date


def get_mat_day(day):
    matrices = _get_mat_with_scheme(str(day))
    return matrices


def get_mat_month(month):
    matrices = _get_mat_with_scheme(str(month))
    return matrices


def _get_mat_with_scheme(scheme, barrier=LAST_CORRECT_DATE):
    scheme = '*{}*.npy'.format(scheme)
    files = glob.glob(os.path.join(DATA_DIR, scheme))
    matrices = []
    for f in files:
        date = extract_date(f)
        if date > barrier:
            mat = get_mat(f)
            matrices.append(mat)
    return matrices


def get_mat(path):
    with open(path, 'r') as f:
        mat = np.load(f)
    return mat
