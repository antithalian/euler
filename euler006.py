# project euler problem #6 solution
# difference between sum of squares of first 100 N and square of sum of same

# sum of first n natural numbers is
# Sn = n(n + 1) / 2 = (n^2)/2 + n/2
sq_sum = (((100 ** 2) / 2) + 50) ** 2

# sum of squares
sum_sq = sum([n ** 2 for n in range(1, 101)])

print(int(sq_sum - sum_sq))