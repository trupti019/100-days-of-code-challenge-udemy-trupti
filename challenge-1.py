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

# import random

# player = int(input("Enter 0/1/2 for rock, paper, scissors respectively: "))

# if player not in [0, 1, 2]:
#     print("Invalid input")
# else:
#     if player == 0:
#         a = 'rock'
#     elif player == 1:
#         a = 'paper'
#     elif player == 2:
#         a = 'scissors'

#     comp = random.randint(0, 2)

#     if comp == 0:
#         b = 'rock'
#     elif comp == 1:  # Corrected to check comp instead of player
#         b = 'paper'
#     elif comp == 2:  # Corrected to check comp instead of player
#         b = 'scissors'

 # if comp == 0:
 #     b = 'rock'
 # elif comp == 1: 
 #     b = 'paper'
 # elif comp == 2:  
 #     b = 'scissors'


#     print(f"The computer chose {b} and you chose {a}")

#     if comp == player:
#         print("It's a tie")
#     elif (comp == 0 and player == 1) or (comp == 1 and player == 2) or (comp == 2 and player == 0):
#         print("You win")
#     else:
#         print("You lose")

# DAY 5 PROGRAMS

# average height

# heights= input("enter the heights of the students in your class: ").split()
# for i in range(0, len(heights)):
#     heights[i]=int(heights[i])
# count=0
# sum=0
# for j in heights:
#     sum += j
#     count+=1
# avg=round(sum/count)
# print(sum)
# print(avg)

# high score

# score= input("enter the scores of students: ").split()
# for i in range(0, len(score)):
#     score[i]= int(score[i])
# print(score)

# hscore=0
# for i in score:
#     if i > hscore:
#         hscore=i

# print(hscore)

# the fizzbuzz game

# for i in range(0,101):
#     if i%3==0 and i%5==0:
#         print('fizzbuzz')    
#     elif i%3==0:
#         print('fizz')
#     elif i%5==0:
#         print('buzz')
#     else:
#         print(i)

# PyPassword generator

# easy level

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# password=[]

# nletters=int(input('enter how many letters do you want: '))
# nnum=int(input('how many numbers: '))
# nsymbols=int(input('how many symbols: '))

# for i in range(0,nletters):
#     password+=random.choice(letters)


# for i in range(0,nnum):
#     password+=random.choice(numbers)

# for i in range(0,nsymbols):
#     password+=random.choice(symbols)

# print(password)
# random.shuffle(password)
# print(password)

# realpw=''
# for i in password:
#     realpw+=i

# print(realpw)

# day 6- code blocks/ identations/ functions/ while loops

# day 7- gang man

# import random

# word_list = [
#     "apple", "banana", "orange", "grape", "kiwi", "strawberry",
#     "watermelon", "pineapple", "blueberry", "raspberry", "peach",
#     "apricot", "pear", "cherry", "mango", "lemon", "lime",
#     "coconut", "papaya", "fig", "plum", "melon", "nectarine",
#     "cranberry", "blackberry", "dragonfruit", "guava", "lychee",
#     "passionfruit", "persimmon", "pomegranate", "tangerine", "mulberry"
# ]

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# ______________
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# ______________
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# ______________
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# ______________''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# endgame = False
# fruit = random.choice(word_list)
# word_length = len(fruit)
# lives = 6
# print(fruit)
# display = ['_' for _ in range(word_length)]

# while not endgame:
#     guess = input("Enter a letter: ").lower()

#     if len(guess) != 1 or not guess.isalpha():
#         print("Please enter a single letter.")
#         continue
    
#     if guess in display:
#         print(f'youvealr guess that letter {guess}')

#     found = False
#     for i in range(word_length):
#         if guess == fruit[i]:
#             display[i] = guess
#             found = True


#     if not found:
#         print(f'{guess} is not there in the given word')
#         lives -= 1
#         if lives == 0:
#             endgame = True
#             print('You lose!')

#     print(" ".join(display))

#     if '_' not in display:
#         endgame = True
#         print('You win!')

#     print(stages[lives])

# day 8 caesar cipher

# positional arguments
# interactive  exercise
# import math
# def paint(height, width,coverage):
#     no_of_cans= f'you  will need {math.ceil((height*width)/coverage)} cans to pain the wall'
#     return no_of_cans

# h=int(input('enter height'))
# w=int(input('enter width'))
# cover=5

# print(paint(height=h, width=w, coverage=cover))

# prime number

# def prime(num):
#     if num==0 or num==1:
#         return 'not prime'
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 return (f'{num} is not a prime number')
#         print(f'{num} is a prime number')

# inp=int(input('enter a number'))
# print(prime(inp))

# final day 8 project

# import string

# alphabets= list(string.ascii_lowercase)

# c_or_d=input('\n type code to enrypt and decode to decrypt----->')
# text= input('enter your message-----> ')
# shift= int(input('enter the shift number----->'))

# def encrypt(plain_text, shift_amount):
#   cipher_text=''
#   for i in plain_text:
#     # shifted_index=(alphabets.index(i)+shift_amount)
#     cipher_text += alphabets[(alphabets.index(i)+shift_amount)%26]
#   print(f'the cipher text is {cipher_text}')

# def decrypt(cipher_text, shift_amount):
#   normal_text=''
#   for i in cipher_text:
#     normal_text+= alphabets[(alphabets.index(i)-shift_amount)%26]
#   print(f'the decrypted text is {normal_text}')


# if c_or_d== 'encrypt':
#   encrypt(plain_text=text, shift_amount=shift)
# elif c_or_d=='decrypt':
#   decrypt(cipher_text=text, shift_amount=shift)

# day 9- dictionaries

# grading exercise

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# print(f'\n {student_scores}')

# student_grades={}

# for i in student_scores:
#     score=student_scores[i]
#     if score>90:
#         student_grades[i]='outstanding'
#     elif score>80:
#         student_grades[i]='Exceeds expectations'
#     elif score>70:
#       student_grades[i]='acceptable'
#     else:
#         student_grades[i]='fail'
# print(student_grades)


# interactive exercise:

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# country=input('enter country: ')
# visits=int(input('enter visits: '))
# cities=(input('enter cities')).split(',')


# def add_new(country,visits,cities):
#     new_country={}
#     new_country['country']=country
#     new_country['visits']=visits
#     new_country['cities']=cities
#     travel_log.append(new_country)

# add_new(country=country, visits=visits, cities=cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f'my favourite city is {travel_log[2]['cities'][0]}')


# secret auction
import os
# dict={}

# def highest_bidder(dict):
#     highest_bid=0
#     winner=''
#     for i in dict:
#         bid_amount= dict[i]
#         if bid_amount>highest_bid:
#             highest_bid=bid_amount
#             winner=i

#     print(f'the winner is{winner}')

# more_bidders=True
# while(more_bidders==True):
#     name=input('enter your name: ')
#     bid_price=int(input('enter your bid price: '))
#     dict[name]=bid_price
#     bidders=input('are there any more bidders? --> ')
#     if bidders=='no':
#         more_bidders=False
#         highest_bidder(dict=dict)

#     elif bidders=='yes':
#         os.system('cls')   

# day 10- docstring and calculator


# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():
  #   num1=float(input('ener first number: '))      #input of first number
#   for i in operations:                          #printing the symbols
#     print(f'{i}')
#   cont=True                                     #initializing flag

#   while cont==True:
#     symbol=input('enter symbol: ')              
#     num2=float(input('enter seconf number: '))
#     func=operations[symbol]                          
#     ans= func(num1, num2)
#     print(f"{num1} {symbol} {num2} = {ans}")

#     if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = ans
#     else:
#       cont = False
#       os.system('cls')
#       calculator()

# calculator()

# day 11- the blackjack capstone project

















