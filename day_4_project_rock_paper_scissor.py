# welcome to the game of rock paper and scissor
import random
print("Welcome to the game of rock paper and scissor!")
user_in = input("What do you choose? Type 0 for Rock, Type 1 for Paper, type 2 for Scissor. ")
print("Your Choice:")
rock ='''
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a
'''
paper ='''

8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88  
'''
scissor = '''
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              
'''
if user_in == '0':
    print(rock)
elif user_in == '1':
    print(paper)
elif user_in == '2':
    print(scissor)
else:
    print("Error, You had entered wrong Input!")

print("Computer Choice:")
computer_in = random.randint(0, 2)
if computer_in == 0:
    print(rock)
elif computer_in == 1:
    print(paper)
elif computer_in == 2:
    print(scissor)
else:
    print("Error, You had entered wrong Input!")
a = int(user_in)
b = int(computer_in)
row1 = ['T', 'L', 'W']
row2 = ['W', 'T', 'L']
row3 = ['L', 'W', 'T']
result_rps = [row1, row2, row3]
if result_rps[a][b] == 'T':
    print("The match is Tie!")
elif result_rps[a][b] == 'W':
    print("Congrats! You won the match. ")
elif result_rps[a][b] == 'L':
    print("Sorry! You loose Better luck next time.")
else:
    print("Error")
