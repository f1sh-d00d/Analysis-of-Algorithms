def mergesort(array):
    '''run mergesort on a given list'''
    sorted_array = []

    if type(array) != list:
        return "Please enter a list"

    if len(array) < 2:
        '''if there is less than 2 elements, the array is sorted by default'''
        sorted_array = array
    
    else:
        mid = int(len(array)/2)
        a = array[:mid]
        b = array[mid:]
        a_sorted = mergesort(a)
        b_sorted = mergesort(b)
        
        print("a: ",a_sorted)
        print("b: ",b_sorted)
        
        sorted_array = merge(a_sorted, b_sorted)

    return sorted_array

def merge(a, b):
    new_array = a+b

    return new_array

    
def main():
    b = [2,4,5,1,3] 
    print(mergesort(b))


main()
