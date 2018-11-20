# booking.com score a list of hotels ordered by average score
#
# input:
# 4
# 1000 8
# 1000 9
# 2000 9
# 2000 9
#
# output:
# 2000
# 1000
# this just sum all scores to order, need to fix average when the number of items are different from other number of items

f = open("hotel.txt","r")

#n = int(raw_input())
n = int(f.readline())
dlist = {}

#for l in range(n):
for l in f:
    #line = raw_input().split()
    line = str(l).split()
    id = line[0]
    ave = int(line[1])
    old = dlist.get(id)

    if dlist.get(id):
        ave = ave + old


    dlist.update( {id : ave} )

#print max(dlist.keys())

f.close()
v = max(dlist.values())

for key, value in dlist.items():
    if value == v:
        print key
#        break




ordered = dlist.keys()
ordered.sort()
for key in ordered:
    print key
