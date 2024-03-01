import sys
sys.set_int_max_str_digits(0) # let python convert arbitrarily long numbers into strings. 


'''
to do:
reformat function "factorial" to use a list
make an even/odd function to split the factorials in half.
make the even and odds work on different threads.
'''


def _factorial(num):
    answer = num
    for i in range(2,num):
        answer *= (i)
    return answer
