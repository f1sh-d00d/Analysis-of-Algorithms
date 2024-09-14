def mergesort(array):
    '''run mergesort on a given list'''
    if type(array) != list:
        print("Please enter a list")
        return

    if len(array) < 2:
        '''if there is less than 2 elements, the array is sorted by default'''
        return array
    
    else:
        mid = int(len(array)/2)
        a = array[:mid]
        b = array[mid:]
        a_sorted = mergesort(a)
        b_sorted = mergesort(b)
        
        print("a: ",a_sorted)
        print("b: ",b_sorted)
        
        return merge(a_sorted, b_sorted)


def merge(a, b):
    max_array = max(a, b, key=len)
    min_array = min(a, b, key=len)
    new_array = []
    i = 0
    j = 0

    for val in min_array:
        if min_array[i] < max_array[j]:
            new_array.append(min_array[i])
            i += 1

        else:
            new_array.append(max_array[j])
            j += 1

    return new_array

    
def main():
    b = [2,4,5,1,3] 
    mergesort(b)


main()
