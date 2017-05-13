def gen_days(year, month, num_of_days):
    first_nine_days = ['0%s' % n for n in xrange(1, 10)]
    rest_days = [str(n) for n in xrange(10, num_of_days+1)]
    days_in_month = first_nine_days
    days_in_month += rest_days
    schemas = ['{}{}{}'.format(year, month, day) for day in days_in_month]
    return schemas

