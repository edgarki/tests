# Given a set of hotels and its guests reviews, sort the hotels based on a list of words specified by a user. The criteria to sort the hotels should be how many times the words specified by the user is mentioned in the hotel reviews.
#
# Input
# The first line contains a space-separated set of words which we want to find mentions in the hotel reviews.
#
# The second line contains one integer M, which is the number of reviews.
#
# This is followed by M+M lines, which alternates an hotel ID and a review belonging to that hotel.
#
# Output
# A list of hotel IDs sorted, in descending order, by how many mentions they have of the words specified in the input.
#
# Notes
# – The words to be find will always be singe words line ‘breakfast’ or ‘noise’. Never double words like ‘swimming pool’.
# – Hotel ud is a 4-byte integer.
# – Words match should be case-insensitive.
# – Dots and commas should be ignored.
# – If a word appears in a review twice, it should count twice.
# – If two hotels have the same number of mentions, they should be sorted in the output based on their ID, smallest ID first.
# – In case one or more test cases time out, consider revisiting the runtime complexity of your algorithms.


#!/bin/python

import math
import os
import random
import re
import sys

import threading
import operator


# Complete the sort_hotels function below.
def sort_hotels(keywords, hotel_ids, reviews):

    # return hotel_ids
    # return reviews

    desc = dict()
    result = dict()
    for i in range(len(hotel_ids)):
        if not desc.has_key(hotel_ids[i]):
            desc[hotel_ids[i]] = []
            result[hotel_ids[i]] = []
        desc[hotel_ids[i]].append(reviews[i])

    # looping for find keywords in description removing non desired grammar punctuation
    def findKW(k, d, g):
        c = 0
        k = k.lower().split(" ")
        d = re.split(r"\.\s*|\s+|!\s*|\?\s*|\,\s*|\:\s*", d.lower())
        for i in range(len(k)):
            for j in range(len(d)):
                if k[i] == d[j]:
                    c += 1
        result[g].append(c)

    # threading for launch the find hotels' description keywords function
    try:
        list_thr = []
        for i in range(len(desc)):
            for j in range(len(desc[i + 1])):
                t = threading.Thread(target=findKW, args=((keywords, desc[i + 1][j], i + 1,)))
                print t
                list_thr.append(t)
                t.start()
                print t
                # t.join()
        # wait for all thread processing
        for t in list_thr:
            t.join()

    except:
        print "error"

    r = {}
    # sum results per hotel ID to score
    for i in range(len(result)):
        for j in range(len(result[i + 1])):
            if j == 0:
                r[i + 1] = int(result[i + 1][0])
            # if j != 0:
            else:
                r[i + 1] = r[i + 1] + int(result[i + 1][j])

    # order results for the most relevant to worst relevant score
    r = sorted(r.items(), key=operator.itemgetter(1), reverse=True)

    # formatting output for given main function
    result = ""
    for i in range(len(r)):
        result += str(r[i][0]) + "\n"
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    keywords = raw_input()

    hotel_ids_count = int(raw_input().strip())

    hotel_ids = []

    for _ in xrange(hotel_ids_count):
        hotel_ids_item = int(raw_input().strip())
        hotel_ids.append(hotel_ids_item)

    reviews_count = int(raw_input().strip())

    reviews = []

    for _ in xrange(reviews_count):
        reviews_item = raw_input()
        reviews.append(reviews_item)

    res = sort_hotels(keywords, hotel_ids, reviews)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
