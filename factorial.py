import sys
import timeit
sys.set_int_max_str_digits(0) # let python convert arbitrarily long numbers into strings. 



def _factorial(num):
    answer = num
    for i in range(2,num):
        answer *= (i)
    return answer


num = 100000


file = open(f'./computed_factorials/{num}_factorial.txt', 'w')
file.write(str(_factorial(num)))
file.close()



'''
Code for timing the execution time. 
'''
# times_run = 1
# result = timeit.timeit(stmt='_factorial(num)', globals=globals(), number = times_run)
# print(f'CPU Execution time: {result/times_run} seconds')
