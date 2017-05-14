import sys

from average import cnt_avg
from minmax import max_mth, min_mth, min_yr, max_yr
from helpers import get_all_days


def main():
    print('Python: {}'.format(sys.version))

    print('Counting average..')
    cnt_avg('months')
    cnt_avg('years')

    print('Counting minimum..')
    min_mth()
    min_yr()

    print('Counting maximum..')
    max_mth()
    max_yr()

    print('Done.')

if __name__ == '__main__':
    # main()
    get_all_days()
