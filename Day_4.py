# I'm writing a function remove duplicate and take list as input and return removing duplicate elements.

def remove_duplicate(L):
    duplicate=set()
    unique_element=[]

    for item in L:
        if item not in duplicate:
            unique_element.append(item)  #append method is used in list to add item in the end of the list
            duplicate.add(item)

        print(duplicate)
    return unique_element


print(remove_duplicate([1,2,2,'e','e',5]))
N={1,1,2,2,3,4,3}
N.add(1)        #add method is used in set and make sure the set doesnot contain duplicates.
print(N)


# I'm writing a function merge list which takes two lists as input and merge them and return them arranging in ascending order

def merge_lists(L1,L2):
    temp=0
    asc=[]
    L=L1+L2
    print(L)
    print(len(L))
    for x in range(len(L)-1):
        for y in range(len(L)-1):
            if L[y]>L[y+1]:
                L[y],L[y+1]=L[y+1],L[y]
            
            
            
    
    return L

print(merge_lists([6,1,5,7,8],[1,2,9,3,7,4]))

