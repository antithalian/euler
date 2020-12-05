# project euler problem #2
# find sum of even valued fibonacci numbers

# more list comprehension go brrrrrrrrrrrrr but with more steps
# basically build a fibonacci generator then list comprehension it
def fib(n):
    f1, f2 = 1, 2
    # try to generate up to n + 1 since we know that the sequence will outgrow n before hitting the nth element
    for _ in range(n + 1):
        if f1 > n:
            break
        else:
            yield f1
            f1, f2 = f2, f1 + f2

print(sum([num for num in fib(4000000) if num % 2 == 0]))