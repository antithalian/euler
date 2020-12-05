# project euler problem #4
# find largest palindrome product of 3 digit numbers

# easiest way to do this in python is probably brute force
# just do all multiplications and then stringify and compare
max = 0
for num1 in range(100, 1000):
    for num2 in range(100, 1000):

        # get string of product
        prd = num1 * num2
        print(prd)
        pal = str(prd)
        # check equality
        if (len(pal) > 5) and ((pal[0] == pal[5]) and (pal[1] == pal[4]) and (pal[2] == pal[3])) and (prd > max):
            max = prd

print(max)
