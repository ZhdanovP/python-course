#To find Pythagorean triple for C less or equal than 100:
#a2 + b2 = c2

import math

maxValue = 100

def gcd(a, b, c = None):
    return ((a if b == 0 else gcd(b, a % b)) if c is None
            else gcd(gcd(a, b), gcd(a, c)))

# m > n, n > 0
#a = m2 - n2
#b = 2 * m * n
#c = m2 + n2

mMax = math.floor(math.sqrt(maxValue - 1))

for m in range(1, mMax + 1):
    for n in range(1, m):
        c = m ** 2 + n ** 2;
        if c > maxValue:
            continue;
        a = m ** 2 - n ** 2
        b = 2 * m * n;
        
        if (gcd(a, b, c) == 1):
            print("{:3}".format(a), "{:3}".format(b),"{:3}".format(c))

