import sys
import time

from average import cnt_avg, cnt_avg_per_day
from minmax import max_mth, min_mth,\
                   min_yr, max_yr, \
                   max_days, min_days


def main():
    print('Python: {}'.format(sys.version))

    t = time.time()
    print('Counting average..')
    cnt_avg('months')
    cnt_avg('years')
    print('Took: {:f} s'.format(time.time()-t))

    t = time.time()
    print('Counting minimum..')
    min_mth()
    min_yr()
    print('Took: {:f} s'.format(time.time()-t))

    t = time.time()
    print('Counting maximum..')
    max_mth()
    max_yr()
    print('Took: {:f} s'.format(time.time()-t))

    print('Done.')


def days():
    print('Average for days...')
    t = time.time()
    cnt_avg_per_day()
    print('Took: {:f}'.format(time.time()-t))

    print('Max for days...')
    t = time.time()
    max_days()
    print('Took: {:f} s'.format(time.time()-t))

    print('Min for days...')
    t = time.time()
    min_days()
    print('Took: {:f} s'.format(time.time() - t))

if __name__ == '__main__':
    days()
    main()
