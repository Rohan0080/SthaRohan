''' I'm writing a function count_Sub_strings() which takes two strings as input and return the count of 
  sub strings in main strings overlapped. And return 0 if the sub string is empty or length of sub 
string is greater than length of main string'''

def count_sub_string(main_string,sub_string):
    if not sub_string or len(sub_string)>len(main_string):
        return 0

    count=0
    for i in range(len(main_string)-len(sub_string)+1):
        if main_string[i:i+len(sub_string)]==sub_string:
            count+=1

    return count

print(count_sub_string("ababababab","aba"))
print(count_sub_string("hello","world"))
print(count_sub_string("blabla","lab"))


''' I'm writing a function find_missing_number taking a list of number and compare with 1to N
as input and return the missing number '''

def find_missing_number(L):
    missing_number=0
    y=0
    x=1
    for i in range(len(L)+1):
        
        if y<len(L) and x==L[y]:
           
            y+=1
        else:
            missing_number=x
        
        x+=1

    return missing_number

print(find_missing_number([1,2,4,5]))

    
        