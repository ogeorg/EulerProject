Cardano's triplet

find triplet a, b, c <= N such that

\sqrt[3]{a+b\sqrt{c}} + \sqrt[3]{a-b\sqrt{c}} = 1

This equation is too compuutationally complicated, so I will transform it to remove the root.  I cube it, which gives me

( a+b\sqrt{c} ) + 3 ( \sqrt[3]{a+b\sqrt{c}} \sqrt[3]{a-b\sqrt{c}} ) ( \sqrt[3]{a+b\sqrt{c}} + \sqrt[3]{a-b\sqrt{c}} ) + (a-b\sqrt{c}) = 1

But the second parentheses of the product is just 1, and we can simplify the first and last term on the left:

2 a + 3 * \sqrt[3]{a+b\sqrt{c}} \sqrt[3]{a-b\sqrt{c}} = 1

Leaving the roots on one side and the rest on the other, and cubing again:

27 ( a+b\sqrt{c} ) ( a-b\sqrt{c} ) = (1 - 2a) ^3

27 ( a^2 - b^2 c ) = 1 - 6a + 12 a^2 - 8 a^3

27 b^2 c = 8 a^3 + 15 a^2 + 6 a - 1  =  (a+1)^2 (8a-1)

c = \frac{ 8 a^3 + 15 a^2 + 6 a - 1 }{ 27 b^2 }  =  c(a,b)



So I do not need 3 loops, only 2 are enough.  We only need to check that the value c is integer, or

(a+1)^2 (8a-1)  mod  (27 b^2)  =  0

moreover, c cannot be less than 1, so we have the additional bound on b

c >= 1

27 b^2  <=  8 a^3 + 15 a^2 + 6 a - 1 

b  <=  \sqrt{ \frac{ 8 a^3 + 15 a^2 + 6 a - 1 }{ 27 } }  =   bmax(a)



So we have 

a  \in  1..N
    b  \in  \min(N-a, bmax(a))
        c(a, b)  must be an integer and c(a,b) <= N-a-b



With this I get:

N=100: 11

1 ---- 2 1 5
2 ---- 5 1 52
3 ---- 5 2 13
4 ---- 8 3 21
5 ---- 11 4 29
6 ---- 14 5 37
7 ---- 17 6 45
8 ---- 17 9 20
9 ---- 17 18 5
10 ---- 20 7 53
11 ---- 23 8 61


N=1000: 149
N=10000: 1632