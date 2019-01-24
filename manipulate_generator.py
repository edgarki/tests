# Enter your code here

def manipulate_generator(g,n):
    z = n+1
    if is_prime_number(z):
        g.next()
        manipulate_generator(g,z)


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(raw_input())
g = positive_integers_generator()
#print g.__sizeof__()
for _ in range(k):
    n = next(g)
    print n
    manipulate_generator(g, n)
#print next(g)
#print next(g)