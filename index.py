print("I'm going to code everyday. Mark my word.")
N=[1,2,3,4,5,6,7,8,9]

def game_visual():
    R1=[  1  ,  2  ,  3 ]
    R2=[  4  ,  5  ,  6 ]
    R3=[  7  ,  8  ,  9 ]
    print(R1)
    print(R2)
    print(R3) 
    return R1,R2,R3

Win=[[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
user_matching_point=0
#choose=print(input("Would you like to go first or second?"))
#if choose=="first":



import random



user=[]
computer=[]
x=5
for game in range(x):  #Making a user to input correct number
    game_visual()
    print("Choose any one of the number: ",N)   
    while True:
         user_input=(int(input()))
         if user_input in N:
             break
         else:
             print("Wrong input. ENter any no from: ",N)
             
    user.append(user_input)  #collecting user input in a list
    
    if user_input in N:
        N.remove(user_input)  #removing user_input from N so that user do not enter those number again
    print(user)

    for sublist in Win:
         user_common_point=set(sublist) and set(user)
         
         if len(user_common_point)>=3:
                user_matching_point+=1

    if user_matching_point>=1:
        print("You won")
        break
    
    if N==[]:  # Making sure when computer cannot get to choose value it skips the else part and print result
            print("No moves left for computer to choose")
    
    else:
        computer_input=random.choice(N)  #Generating a random no from N
        print("computer chooses ", computer_input)
        computer.append(computer_input)
        if computer_input in N:
            N.remove(computer_input)
        print(computer)

    

    
    computer_matching_point=0
    
    for sublist in Win:
         '''user_common_point=set(sublist) and set(user)
         
         if len(user_common_point)>=3:
            user_matching_point+=1'''

         computer_common_point=set(sublist) and set(computer)
         if len(computer_common_point)>=3:
            computer_matching_point+=1

    

    if computer_matching_point>=1:
        print("Computer won")
        break

    if N==[]:
        print("Draw.... Nobody won this game")
    


    




   



    


    
