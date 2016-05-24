from math import sqrt, floor

one_third = 1/3.0
def cardano(a, b, c):
    bc = b * sqrt(c)
    k1 = a + bc
    k2 = a - bc
    if k2 >= 0:
        return k1 ** one_third + k2 ** one_third
    else:
        return k1 ** one_third - (-k2) ** one_third

r = lambda a: ((8*a + 15)*a + 6)*a - 1
s = lambda b: 27 * b*b

N = 100
i = 0
for a in range(1, N+1):
    ra = r(a)
    bmax = int(min(  floor(sqrt(ra / 27.0))  ,  N-a  ))

    if ra%27 != 0:
        continue
    # print "----------------", a, ra, ra%27, bmax

    for b in range(1, bmax+1):
        sb = s(b)
        if ra % sb == 0:
            c = ra / sb
            if c <= N-a-b:
                i += 1
                print i, "----", a, b, c# , a+b+c, cardano(a, b, c)


print i