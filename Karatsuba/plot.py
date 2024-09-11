import math
import matplotlib.pyplot as plt
import sys
import time
import random
import matplotlib.pyplot as plt


def plot():

    maxes = [9, 99, 9999, 99999999]
    mins = [1, 10, 1000, 10000000]

    karatsuba_times = []
    classic_times = []

    for i in range(4):
        min_len = mins[i]
        max_len = maxes[i]

        x = str(random.randint(min_len, max_len))
        y = str(random.randint(min_len, max_len))

        k_start = time.time()
        karatsuba(x, y)
        k_end = time.time()
        k_time = k_end - k_start
        karatsuba_times.append(k_time)

        c_start = time.time()
        classic(int(x), int(y))
        c_end = time.time()
        c_time = c_end - c_start
        classic_times.append(c_time)

    fig, ax = plt.subplots()
    
    ax.plot(karatsuba_times, label='Karatsuba')
    ax.plot(classic_times, label='Classic')
    plt.show()
    print(karatsuba_times)
    print(classic_times)



def classic(num1, num2):
    result = 0
    for i in range(num1):
        result += num2
    return result


def transform(num_string):
    '''given a number that is a string, take the length of the string and check to see if it is a factor of two.
    if it is not a factor of two find the nearest length greater than the current length that is a factor of two
    and backfill the number with zeros to make it that length'''
    num_len = len(num_string)
    
    #if the length is already a factor of two, no need to backfill
    if math.log2(num_len).is_integer():
        return num_string
    else:
        exact_log = math.log2(num_len)
        remainder = math.log2(num_len) % 1
        next_log = exact_log - remainder + 1
        needed_zeros = 2**(next_log) - num_len

        zeros = "0" * int(needed_zeros)
        transformed_num = zeros + num_string
        return transformed_num


def match(target, num):
    '''given two numbers as strings, backfill num with zeros so that it is the same length as the target'''
    needed_zeros = len(target) - len(num)
    zeros = "0" * needed_zeros
    matched_num = zeros + num
    return matched_num



def karatsuba(num1, num2):
    '''recursively compute the product of two numbers using Karatsuba's algorithm
        n = number of digits in largest number

        given inputs x and y
        split x and why into even halfs, a,b,c,d respectively

        a*b*c*d = (a+b)(c+d) - ac - bd

        product = 10^n*ac + 10^(n/2)*abcd + bd'''
    #backfill input numbers as needed
    x = transform(num1)
    y = transform(num2)
    
    #make sure input numbers are the same length
    if len(x) > len(y):
        fixed_num = match(x, y)
        y = fixed_num
    elif len(y) > len(x):
        fixed_num = match(y, x)
        x = fixed_num
    
    #print(len(x), len(y))
    #print(len(x) == len(y))

    digits = len(x)

    #if the inputs only have 1 digit, just multiply them normally
    if digits == 1:
        return int(x) * int(y)

    else:

        mid = int(len(x)/2)

        #print(digits)
        #print(mid)
    
        #split numbers in half
        a = x[:mid]
        b = x[mid:]
        c = y[:mid]
        d = y[mid:]

        #nums = [a,b,c,d]

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        p = int(a) + int(b)
        q = int(c) + int(d)
        
        #transform middle terms
        p = transform(str(p))
        q = transform(str(q))

        #make sure the middle terms have the same length
        if len(p) > len(q):
            fixed_num = match(p, q)
            q = fixed_num
        elif len(q) > len(p):
            fixed_num = match(q, p)
            p = fixed_num

        #print(p)
        #print(q)

        pq = karatsuba(p, q)

        #final step of calculating middle term
        abcd = pq - ac - bd

        result = 10**(digits) * ac + 10**(mid) * abcd + bd

        return result

'''
def main():
    k_start = time.time()
    result = karatsuba(sys.argv[1], sys.argv[2])
    k_end = time.time()
    k_time = k_end - k_start
    print(result)
    print("Karatsuba took ", k_time, " seconds\n")
    
    c_start = time.time()
    product = classic(int(sys.argv[1]), int(sys.argv[2]))
    c_end = time.time()
    c_time = c_end - c_start
    print(product)
    print("Classic multiplication took ", c_time, " seconds\n")
'''

def main():
    plot()

main()

