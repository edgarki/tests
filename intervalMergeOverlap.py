# booking.com enter a list of intervals and merge if have overlaps
#
#input:
# 3
# 10 20
# 8 17
# 30 40
#
#output:
# 1
# 8 20
# 30 40


# Complete the function below.


def merge_overlapping_intervals():
    n = int(raw_input())
    lista = []
    for i in range(n):
        line = raw_input().split()
        lista.append((int(line[0]), int(line[1])))


    o = sorted(lista, key=lambda tup: tup[0])

    merged = []

    for tup in o:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = tuple([b[0], tup[1]])
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    z = len(merged)
    print z
    for j in range(z):
        print str(merged[j][0]) + " " + str(merged[j][1])

merge_overlapping_intervals()


