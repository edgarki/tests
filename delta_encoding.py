# input example
# 8
# 25626
# 25757
# 24367
# 24267
# 16
# 100
# 2
# 7277
#
# output
# 25626
# -128
# 131
# -128
# -1390
# -100
# -128
# -24251
# 84
# -98
# -128
# 7275
#
#


#!/bin/python

import sys
import os



# Complete the function below.

def delta_encode(array):
    esc = -128
    before = array[0]
    result = []
    result.append(before)
    for i in range(len(array)):
        d = array[i] - before
        if ( abs(d) > 127 ):
            result.append(esc)
        if (d != 0):
            result.append(d)
        before = array[i]
    return result


if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    array_cnt = 0
    array_cnt = int(raw_input())
    array_i = 0
    array = []
    while array_i < array_cnt:
        array_item = int(raw_input());
        array.append(array_item)
        array_i += 1


    res = delta_encode(array);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()
