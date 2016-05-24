from primes import Primes     
import time
import math

def make_fun(a, b):
    """
    Returns a function with coeff a and b
    Function is "loaded" with its coeffs and a formating function
    """
    def f(n):
        return n*n + a*n + b

    f.a = a
    f.b = b
    f.format = lambda: "n^2 %s %d n %s %d" % (
        a>0 and '+' or '-', math.fabs(a),
        b>0 and '+' or '-', math.fabs(b),
        )
    return f


# N ==  4 : creates from -3 to +3, a range of 2N-1
# a == -3 : i = 0 = a+N-1
# a ==  0 : i = 3 = a+N-1
# a ==  3 : i = 6 = a+N-1

def get_coeffs(N):
    """
    Generators of all pairs of integers within a square
    from [-(N-1),-(N-1)] to [N-1,N-1].  Each "onion shell"
    starts at [i.0] and goes counterclockwise
    """
    ts = time.time()
    for a in range(N):
        #  
        # +   2   +
        #  \  |  /
        #   \ | / 1
        #    \|/
        # 3---*---+
        #    /|\
        #   / | \ 5
        #  /  |  \
        # +   4   +

        # 1
        for b in range(a):
            yield a, b
        
        # 2
        for b in range(2*a):
            yield a-b, a

        # 3
        for b in range(2*a):
            yield -a, a-b
        
        # 4
        for b in range(2*a):
            yield -a+b, -a

        # 5
        for b in range(a):
            yield a, -a+b

        # Prints the time needed to covers the onion shell
        ts2 = time.time()
        print (a, ts2-ts)
        ts = ts2


N = 1000        # N is half the side
L = 2*N-1       # L is the side of the square

# Creates a matrix, initialized to 0
# Each elements will represent the number of primes generated
matrix = [[0]*L for i in range(L)]


# Primes generator
primes = Primes()

# For the moment the maximum sequence has 0 length
# Each time we find a longer sequence we will record it here
# together with its parameters (point in the square, ...)
maxi = {'n': 0}

for a, b in get_coeffs(N):
    i = a + N - 1       # indices in the matrix
    j = b + N - 1   

    f = make_fun(a, b)

    # how many primes does f produces?
    n = 0
    while True:
        p = f(n)
        if not primes.is_prime(p):
            break
        else:
            pass
        n += 1

    # records number of primes in the matrix
    matrix[i][j] = n

    # if we have found a better sequence, we save it in 'maxi'
    if n > maxi['n']:
        maxi = {'n': n, 'f': f}
        print (f.format(), " ------> ", maxi['n'])

#    print ("===============================================================", a, b, n)

print (maxi['f'].format(), " ------> ", maxi['n'])

f = maxi['f']
for i in range(maxi['n']):
    print (i, f(i))



# Now we make an image from the matrix
from PIL import Image
im = Image.new('RGB', (L,L), 'white')

nmax = maxi['n']
for i in range(L):
    for j in range(L):
        n = 256 - int(matrix[i][j] * 256 / nmax)
        im.putpixel((j,i), (n,n,n))

im.save('images/%dx%d.png' % (L,L))

