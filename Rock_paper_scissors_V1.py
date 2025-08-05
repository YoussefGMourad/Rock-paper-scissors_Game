import random


choices=('r','p','s')
Score=0
while True:
    
    User_input=input("Rock,Paper,Cross: (r,p,s): ").lower()
    Computer_input=random.choice(choices)

    
    
    if User_input not in choices:
        print("wrong input")
        continue
   
    print('your choice is ',{User_input})
    print('Comp choice is ',{Computer_input})
    
    if User_input==Computer_input:
        print("tie")
    elif (
        (User_input =='r' and Computer_input == 's') or
        (User_input =='p' and Computer_input == 'r') or
        (User_input =='s' and Computer_input == 'p')
        ):
        Score = Score+1
        print("you won")
    else:
       
        print("you lose")
    
    
    Play=input("Play again? (y/n) ").lower()
    if Play == 'n':
        print("thanks")
        print("the final score is" ,Score)
        break