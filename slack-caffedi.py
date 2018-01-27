# -*- coding: utf-8 -*-

import datetime

CHANNEL_OR_USERNAME = '#example'

if __name__ == "__main__":
    current_year = datetime.datetime.now().year
    for month in range(1, 13):
        for day in range(1, 8):
            examined_day = datetime.datetime(current_year, month, day)
            if examined_day.isoweekday() == 1:
                print '/remind {} caffedi on {} {}'.format(CHANNEL_OR_USERNAME, examined_day.strftime("%B"), examined_day.day)
                break
