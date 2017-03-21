import datetime

__author__ = 'kenneth'


def get_preg_date(weeks):
    days = int(weeks) * 7
    p_date = datetime.datetime.today() - datetime.timedelta(days=days)
    return p_date.strftime("%a, %d %b %Y %H:%M:%S GMT")