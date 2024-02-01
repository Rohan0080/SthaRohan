'''x=[1,2,3,4,5,6,7,8,9]
user=[]
for y in range(5):
#    x.append(int(input()))
 #   print(x)

    user_input=(int(input()))
    user.append(user_input)
    if user_input in x:
        x.remove(user_input)
    else:
        print("Not found")

    print(user)
    print(x)
    '''

'''while True:
    user_input = input("Enter a number between 1 and 10: ")
    
    # Check if the input is a number between 1 and 10
    if user_input.isdigit() and 1 <= int(user_input) <= 10:
        # Convert the input to an integer
        number = int(user_input)
        print("You entered:", number)
        break  # Exit the loop if the input is valid
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
'''
N=[]
if N==[]:
         print("Draw... Nobody wins the game") 