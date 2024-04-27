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
# import os
# # dict={}

# # def highest_bidder(dict):
# #     highest_bid=0
# #     winner=''
# #     for i in dict:
# #         bid_amount= dict[i]
# #         if bid_amount>highest_bid:
# #             highest_bid=bid_amount
# #             winner=i

# #     print(f'the winner is{winner}')

# # more_bidders=True
# # while(more_bidders==True):
# #     name=input('enter your name: ')
# #     bid_price=int(input('enter your bid price: '))
# #     dict[name]=bid_price
# #     bidders=input('are there any more bidders? --> ')
# #     if bidders=='no':
# #         more_bidders=False
# #         highest_bidder(dict=dict)

# #     elif bidders=='yes':
# #         os.system('cls')   

# # day 10- docstring and calculator


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
#     num1=float(input('ener first number: '))      #input of first number
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
# import random

# yorn=input(print('do u want to play the game type "y" or "n" : '))
# if yorn=='y':

#     def return_random_card():
#         cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#         card=random.choice(cards)
#         return card
    
#     def calculate_score(list):
#         summ=0
#         for i in list:
#             summ+=i
    
#     user=list(random.sample(cards,2))
#     computer=list(random.sample(cards,2))
#     compsum=sum(computer)
#     usersum=sum(user)


# day 12 number guessing game

# print('''i AM THE THINKER
#       I AM THINKING ABOUT A NUMBER BETWEEN 1 AND 100''')

# import random
# comp=random.randint(0,101)
# # print(f'psssst the number is : {comp}')

# def diff():
#     difficulty= input('\n choose a difficulty: easy or hard: \n ')
#     if difficulty=='easy':
#         attempts=10

#     elif difficulty=='hard':
#         attempts=7

#     else:
#         print('Invalid choice, defaulting to easy.')
#         attempts = 10
    
#     return attempts

# guess=False
# attempts= diff()


# def check(user, comp, attempts):
#             global guess
#             if user!=comp:
#                 attempts-=1
#                 if user>comp:
#                     print('\n too high ')
#                 if user<comp:
#                     print('\n too low')
#                 if attempts == 0:
#                     print('You ran out of attempts.')
#                     guess = True
#             elif user==comp:
#                 guess=True
#                 print('\n u have guess the right number')


# while attempts!=0 and guess==False:
#         print(f'\n you have{attempts} attempts left to guess the number')
#         user=int(input('\n make a guess: '))
#         check(user, comp, attempts)


# day 13 debugging

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num-1])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <1994:
#   print("You are a millenial.")
# elif year >=1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Higher or lower
import os

logo = 'HIGHER OR LOWER'

vs = """   __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

def follower_count(a,b):

    
    if a['follower_count']>b['follower_count']:
        return 'A'
    elif b['follower_count']>a['follower_count']:
        return 'B'
    else:
        return 'nein'
global b 
b =random.choice(data)
def game(data):
    score=0
    
    while True:

        print(logo)
        global b
        a= b
        b= random.choice(data)
        if a==b:
            b=random.choice(data)

        print(f"compare A:  {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B:  {b['name']}, a {b['description']}, from {b['country']}.")
        user_inp=input('who has more follower coun?? Type A OR B :').strip().upper()
        result= follower_count(a,b)
        os.system('cls')
        if user_inp ==result:
            score= score+1
            print(f'correct guess!! Score: {score}')

        else:
            print(f'''incorrect guess >_<. 
                the follower count of  {a['name']} is {a['follower_count']}  and 
                the follower count of  {b['name']} is {b['follower_count']}''')
            print(f'FINAL SCORE ---- {score}')
            break
        
    play_again=(str(input('do u want to play again: '))).strip().lower()
    if play_again=='yes':
        game(data)


game(data)