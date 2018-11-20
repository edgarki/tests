square = 0
rectangle = 0
neither = 0

def check(input):
    global square, rectangle, neither
    for i in range(6):

        polygon_sides = list(map(int, input.split()))
        if any(side < 0 for side in polygon_sides):
            neither = neither + 1
        else:
            if len(set(polygon_sides)) == 1:
                square = square + 1
            elif len(set(polygon_sides)) == 2:
                if polygon_sides[0] == polygon_sides[2] and polygon_sides[1] == polygon_sides[3]:
                    rectangle = rectangle + 1
                else:
                    neither = neither + 1
            else:
                neither = neither + 1

    #return (' '.join(map(str, [square, rectangle, neither])))
    #return [square, rectangle, neither]


f = open("polygons.txt","r")

for line in f:

    #print line
    check(line)

print (' '.join(map(str, [square/6, rectangle/6, neither/6])))


f.close()