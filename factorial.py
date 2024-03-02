import sys
sys.set_int_max_str_digits(0) # let python convert arbitrarily long numbers into strings. 



def _factorial(num):
    answer = num
    for i in range(2,num):
        answer *= (i)
    return answer
