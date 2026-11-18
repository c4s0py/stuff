def bubble_sort(unsorted_list):
    nlist = len(unsorted_list)
    
    for i in range(nlist):
        
        swapped = False
        
        
        for x in range(nlist - 1 - i):
            
            
            if unsorted_list[x] > unsorted_list[x+1]:
                unsorted_list[x], unsorted_list[x+1] = unsorted_list[x+1],unsorted_list[x]
                swapped = True
                
        if not swapped:
            break

unsorted_list = [104, 3422, 98942, 196, 595, 82395, 2018, 63850, 4345, 10256]
bubble_sort(unsorted_list)

print(unsorted_list)
