import random


choices=('r','p','s')
Score=0

def Get_Userinput():
    while True:
        User_input=input("Rock,Paper,Cross: (r,p,s): ").lower()
        if User_input in choices:
           return User_input
        else:
           print("wrong input")
           
def CP_input():
   return random.choice(choices)

def Display(U_input,Comp_input):
    print('your choice is ',{U_input})
    print('Comp choice is ',{Comp_input})

def winner(U_input,Comp_input,score):
    
    if U_input==Comp_input:
        print("tie")
        
    elif (
        (U_input =='r' and Comp_input == 's') or
        (U_input =='p' and Comp_input == 'r') or
        (U_input =='s' and Comp_input == 'p')
        ):
        Score += 1
        print("you won")
    else:
       
        print("you lose")
        return score
   
def Play_again():
    while True:
        Play = input("Play again? (y/n): ").lower()
        if Play == 'y':
            return True     # continue playing
        elif Play == 'n':
            return False    # stop playing
        else:
            print("Invalid input. Please enter y or n.")

        
while True:
    U_input=Get_Userinput()
    
    Comp_input=CP_input()
    
    Display(U_input,Comp_input)
    
    if U_input not in choices:
        print("wrong input")
        continue
    
    Score = winner(U_input, Comp_input, Score)
    
    if not Play_again():
         print("your score is", Score) 
         break
    
    
   
    
        
        
        
        