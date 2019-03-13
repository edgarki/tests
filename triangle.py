# check triangle
#0: no triangle
#1: equilateral
#2: not equilateral

def triangle(a, b, c):
    if ( a+b > c and a+c > b and b+c > a ):
        if ( a+b == c and a+c == b and b+c == a or ( a == b and b == c and a == b ) ):
            return 1
        return 2
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(raw_input().strip())

    b = int(raw_input().strip())

    c = int(raw_input().strip())

    res = triangle(a, b, c)

    fptr.write(str(res) + '\n')

    fptr.close()
