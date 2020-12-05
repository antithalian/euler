# project euler problem 5
# smallest multiple divisible by 1 through 20

from math import gcd

# lcm is from python 3.9 and I've got 3.8.5 sadly
def lcm(x, y):
    return int((x * y) / gcd(x, y))

num = 1
for itr in range(1, 21):
    num = lcm(num, itr)

print(num)