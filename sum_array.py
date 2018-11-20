# version 1

from collections import OrderedDict

array = []

f = open("sum_array.txt","r")

n = int(f.readline())
m = int(f.readline())

for l in f:
    array.append(int(l))


f.close()

#print array



pairs = OrderedDict()

out = 0
for value in array:
    number = pairs.get(value)
    if number or number == 0:
        out=1
    else:
        pairs[n-value] = value

print out


# version 2
def find_sum(number_map):
    for key in number_map:
        if number_map.get(key) in number_map.keys():
            #print number_map.get(key)
            return 1
    return 0




f = open("sum_array.txt","r")

n = int(f.readline())
m = int(f.readline())
number_map = {}
for i in range (m):
    z = int(f.readline())
    number_map.update({ z : abs(n - z)})
#print(find_sum(number_map))

#print number_map


for key in number_map:
    if number_map.get(key) in number_map.keys():
        print 1
        break

f.close()




# version 3



f = open("sum_array.txt","r")

#n = int(raw_input())
n = int(f.readline())
#m = int(raw_input())
m = int(f.readline())
dlist = {}

for l in f:
    z = int(l)
    dlist.update( {z : abs (n - z)} )


f.close()

#for i in range(m):
#    z = int(raw_input())
#    dlist.update( {z : abs(n-z)})

#print dlist
o = 0
for j in dlist:
    if dlist.get(j) in dlist.keys():
        #print dlist.get(j)
        o = 1
        break

print o

