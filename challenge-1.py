import random

# print("this is the band name generator program")
# city= input("enter the name of a city: ")
# pet= input("enter the name of your pet: ")
# print("your band name could be {} {}".format(city, pet))

# print("This is the tip calculator")
# bill=int(input("enter your bill amount in $ : "))
# tip=int(input("how much do u want to tip (10, 20, 30) : "))
# persons= int(input("how many people are splitting the bill: "))
# per_person=(bill+tip)/persons
# print("each person has to pay ${}".format(per_person))

# python pizza
# finalp=0
# size= input("what size pizza do u prefer my lord? (S, M, L)")
# if size=='S':
#     finalp+=15
# elif size=='M':
#     finalp+=20
# elif size=='L':
#     finalp+=25

# pep=input("do u need peproni on your pizza your grace? (type Y or N): ")
# if size=='S'and pep=='Y':
#     finalp+=2
    
# elif size=='M' or size=='L' and pep=='Y':
#     finalp+=3

# cheese=input("extra cheese?? ")
# if cheese=='Y':
#     finalp+=1

# print("thankyou for choosing python pizza your bill is {}".format(finalp))
    
# LOVE CALCULATOR

# name1=input("enter name 1: ").lower()
# name2=input("entername 2: ").lower()
# combined_names = name1+name2
# count1=0
# count2=0

# for i in 'true':
#     count1+= combined_names.count(i)


# for j in 'love':
#     count2+= combined_names.count(j)

# print(count1)
# print(count2)

# score = int(str(count1)+ str(count2))
# print("your score is ", score)

# DAY 3 CHALLENGE

# print('WELCOME TO TREASURE ISLAND\n do u want to go left or right?')
# a=input()
# if a=='right':
#     print('game over')
# elif a=='left':
#     b=input('swim or wait?')
#     if b=='swim':
#         print('game over')
#     elif b=='wait':
#         c=input('which door?')
#         if c=='red' or c=='blue':
#             print('game over!')
#         elif c=='yellow':
#             print('you win')

# day 4

# a= random.randint(0,2)
# if a==0:
#     print('heads')
# else:
#     print('tails')

# banker roullette

# names= str(input('Enter the names of people: '))
# names_list= names.split(", ")
# length= len(names_list)
# rand= random.randint(0, length-1)
# print(f'the person to pay the bill is {names_list[rand]}')

# Treasure island

# map=[[" "," "," "],
#      [" "," "," "],
#      [" "," "," "]]
# print("the map is made up of 3x3 blocks, pls enter co-ordinates of the block: ")
# coords= input()
# coords.lower()
# abc=["a","b","c"]
# alpha=coords[0]
# a=abc.index(alpha)
# numeric=int(coords[1])
# b=numeric-1
# map[a][b]="X"
# print(map)

# FINAL DAY 4 PROJECT- rock paper sciccors

import random

player = int(input("Enter 0/1/2 for rock, paper, scissors respectively: "))

if player not in [0, 1, 2]:
    print("Invalid input")
else:
    if player == 0:
        a = 'rock'
    elif player == 1:
        a = 'paper'
    elif player == 2:
        a = 'scissors'

    comp = random.randint(0, 2)

    if comp == 0:
        b = 'rock'
    elif comp == 1: 
        b = 'paper'
    elif comp == 2:  
        b = 'scissors'

    print(f"The computer chose {b} and you chose {a}")

    if comp == player:
        print("It's a tie")
    elif (comp == 0 and player == 1) or (comp == 1 and player == 2) or (comp == 2 and player == 0):
        print("You win")
    else:
        print("You lose")



