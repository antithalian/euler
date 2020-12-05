# project euler problem #4
# find largest palindrome product of 3 digit numbers

# easiest way to do this in python is probably brute force
# just do all multiplications and then stringify and compare
max = 0
for num1 in range(999, 99, -1): # go to 999 since non inclusive of last
    for num2 in range(999, 99, -1):

        # get string of product
        prd = num1 * num2
        pal = str(prd)
        # check equality
        # had forgotten about the magic of python string slicing - can reverse strings that way
        if (pal == pal[::-1]) and (prd > max):
            max = prd

print(max)
