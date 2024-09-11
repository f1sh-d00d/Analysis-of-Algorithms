import math
import sys

def transform(num_string):
    num_len = len(num_string)
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


def karatsuba(num1, num2):
    '''Recursively performs karatsuba multiplication. Keep in mind that num1 and num2 are technically strings'''
    #print("num1: ", num1, " num2: ", num2)

    if (len(num1) == 1 or len(num2) == 1):
        return int(num1) * int(num2)
    else:
        #transformed num1 & num 2
        num_1 = transform(num1)
        num_2 = transform(num2)
        #print("num_1: ",num_1," num_2: ", num_2)
        #print(len(num_1) == len(num_2))

        '''if int(num1) <= int(num2):
            mid = int(len(num_1)/2)
        else:
            mid = int(len(num_2)/2)'''


        mid = int(len(num_1)/2)
        
        a = num_1[:mid]
        b = num_1[mid:]
        c = num_2[:mid]
        d = num_2[mid:]
        #print(d)

        p = str(int(a) + int(b))
        q = str(int(c) + int(d))

        x=karatsuba(a,c)
        z=karatsuba(b,d)
        y=karatsuba(p,q) - x - z

        num_digits = len(num1)
        half_digits = int(len(num1)/2)
        
        product = ((10**(num_digits))*x) + ((10**(half_digits))*y) + z
        return product



def main():
    num1 = transform(sys.argv[1])
    num2 = transform(sys.argv[2])
    print(karatsuba(num1, num2))
 

main()
