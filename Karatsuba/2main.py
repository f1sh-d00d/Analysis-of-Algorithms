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

def match(target, num):
    needed_zeros = len(target) - len(num)
    zeros = "0" * needed_zeros
    matched_num = zeros + num
    return matched_num


def karatsuba(num1, num2):
    x = transform(num1)
    y = transform(num2)

    if len(x) > len(y):
        fixed_num = match(x, y)
        y = fixed_num
    elif len(y) > len(x):
        fixed_num = match(y, x)
        x = fixed_num
    
    #print(len(x), len(y))
    #print(len(x) == len(y))

    digits = len(x)

    if digits == 1:
        return int(x) * int(y)

    else:

        mid = int(len(x)/2)

        #print(digits)
        #print(mid)

        a = x[:mid]
        b = x[mid:]
        c = y[:mid]
        d = y[mid:]

        #nums = [a,b,c,d]

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        p = int(a) + int(b)
        q = int(c) + int(d)

        p = transform(str(p))
        q = transform(str(q))

        if len(p) > len(q):
            fixed_num = match(p, q)
            q = fixed_num
        elif len(q) > len(p):
            fixed_num = match(q, p)
            p = fixed_num

        #print(p)
        #print(q)

        pq = karatsuba(p, q)

        abcd = pq - ac - bd

        result = 10**(digits) * ac + 10**(mid) * abcd + bd

        return result


def main():
    result = karatsuba(sys.argv[1], sys.argv[2])
    print(result)
    check = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    print(result == check)


main()

