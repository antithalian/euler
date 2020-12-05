# project euler problem #1
# find sum of multiples of 3 or 5 below 1000

# lol list comprehension go brrrrrrrrrrrrrrr
print(sum([num for num in range(1000) if num % 3 == 0 or num % 5 == 0]))