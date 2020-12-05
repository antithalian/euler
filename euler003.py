# project euler problem #2
# find largest prime factor of 600851475143

number = 600851475143

# just brute force it...
n = 2
# intuitively, we only have to check up to sqrt of number
while (n ** 2) < number:

    # if number is divisible by the current n, divide number by that n
    while number % n == 0:
        number = number / n
    n += 1

print(int(number))