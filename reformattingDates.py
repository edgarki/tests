#!/bin/python

import math
import os
import random
import re
import sys

from datetime import datetime


#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def reformatDate(dates):
    for i in range( dates.__len__() ):
        if dates[i].__len__() < 13:
            dates[i] = str(0) + dates[i]
        day = dates[i].split()[0][:2]
        dates[i] = dates[i].split()
        dates[i][0] = day
        dates[i] = ' '.join(dates[i])
        dates[i] = datetime.strptime(dates[i], '%d %b %Y').strftime("%Y-%m-%d")

    return dates


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(raw_input().strip())

    dates = []

    for _ in xrange(dates_count):
        dates_item = raw_input()
        dates.append(dates_item)

    result = reformatDate(dates)

    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()
