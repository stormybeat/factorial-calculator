import sys
sys.set_int_max_str_digits(0) # let python convert arbitrarily long numbers into strings. 

'''
to do:
    make an split list function to split the number to make a factorial of in half.
    make them all use different threads.
'''

def _em2generateLists(generationInput):
    generationOutput = []
    for i in range(1, generationInput + 1):
        generationOutput.append(i)
    return generationOutput


    
def _em2factorial(listInput):
    answer = 1
    for i in listInput:
        answer *= (i)
    return answer


print(_em2generateLists(10))
