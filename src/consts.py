import os

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SRC_DIR, '..')
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
TEST_DIR = os.path.join(PROJECT_DIR,'tests')
OUT_DIR = os.path.join(PROJECT_DIR, 'out')
OUT_MONTHS_DIR = os.path.join(OUT_DIR, 'months')
OUT_YEARS_DIR = os.path.join(OUT_DIR, 'years')

YR_FILE = '201405-201505.csv'


AVG_MONTHS_DIR = os.path.join(OUT_MONTHS_DIR, 'avg')
MAX_MONTHS_DIR = os.path.join(OUT_MONTHS_DIR, 'max')
MIN_MONTHS_DIR = os.path.join(OUT_MONTHS_DIR, 'min')

AVG_YEARS_DIR = os.path.join(OUT_YEARS_DIR, 'avg')
MAX_YEARS_DIR = os.path.join(OUT_YEARS_DIR, 'max')
MIN_YEARS_DIR = os.path.join(OUT_YEARS_DIR, 'min')

LAST_CORRECT_FILE = 'gfsanl_4_20160511_1200_000.grb2.npy'
LAST_CORRECT_DATE = '20160511'
ARRAY_SIZE = (361, 720)

MONTHS = [
    '201704',
    '201703',
    '201702',
    '201701',
    '201612',
    '201611',
    '201610',
    '201609',
    '201608',
    '201607',
    '201606',
    '201605',
]

# test consts
TEST_FILE = LAST_CORRECT_FILE
NUM_OF_DATA_FOR_A_DAY = 4
NUM_OF_DATA_FOR_APRIL = 114
