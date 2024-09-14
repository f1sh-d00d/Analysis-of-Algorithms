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
    new_array = []

    '''compare first elements in each array. remove smallest and add it to new array. do this til one list runs out'''
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            new_array.append(a.pop(0))

        else:
            new_array.append(b.pop(0))
    
    '''since one list is empty, these loops will add the remaining elements in a or b to the new array, and it will automatically be sorted'''
    for i in range(len(a)):
        new_array.append(a.pop(0))
    
    for i in range(len(b)):
        new_array.append(b.pop(0))
    
    print(new_array)
    return new_array

    
def main():
    b = [2,4,5,1,3] 
    print(mergesort(b))


main()
