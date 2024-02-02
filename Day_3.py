# Taking a input from user in a function  and return true if palindrome else false.

def palindrome(s):
    
    
    s=''.join(char.lower() for char in s if char.isalnum() )


    return s==s[::-1]
    
    
print(palindrome("Madam"))
print(palindrome("A man, a plan, a canal, panama"))
print(palindrome("hello"))


#Write a function count_vowels() which take a string as input and returns vowel count.

def count_vowels(s):
    count=0
    v=['a','e','i','o','u','A','E','I','O','U']
    
    for char in s:
        if char in v:
            count+=1
    
    return count
    
   


print(count_vowels("Python Programming"))
print(count_vowels("Javascript"))


#Write a function that takes a list as input and return unique elements

def unique_elements(L):
    unique_list=[]
    for char in L:
        if char not in unique_list:
            unique_list.append(char)
    return unique_list

print(unique_elements([1,3,2,3,2,4,5,2,4]))
print(unique_elements(['a', 'b', 'a', 'c', 'd', 'b']))


# Write a function find_max_occurence and takes list as input and returns max occurence

def find_max_occurence(L):
    max_occurence=0
    max_element=0
    for element in set(L):
        count=L.count(element)
        if count>max_occurence:
            max_occurence=count
            max_element=element

    return max_element
    
                

    

print(find_max_occurence([1,2,2,3,3,3,4,4,4]))


