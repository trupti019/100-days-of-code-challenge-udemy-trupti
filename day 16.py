# oop in python-- day 16 coffee machine using oop

# when we have more complex programs procedural programming 
# might not be the best way to do it

'''  object:   
things that they have --- attributes
things hat they do ---- methods modelled by functions

we can geneerate multiple versions of the same object like a blueprint
we call this blueprint a class and the individual obj are objects

=> creating a class and object

car= CarBlueprint()
|           |
object     class

car.speed-- speed is the attribute

python packages-- alr written code
Py PI -- python package index
pretty table library



''' 
# from turtle import Turtle, Screen
# chigga= Turtle()                         # chigga is an object of the class turtle  
# print(chigga) 
# chigga.shape(name='turtle')
# chigga.color("coral","green")

# chigga.forward(100)

# my_screen= Screen()                         #created a object
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table= PrettyTable()
# poke_dict={}
# num=int(input('how many pokemons would u like to enter: '))
# for i in range(0,num):
#     poke_type= input('enter pokemon and its type (pokemon: type) :')
#     poke, type= poke_type.split(":")
#     poke_dict[poke.strip()]= type.strip()

# print(poke_dict)

# keys= list(poke_dict.keys())
# values= list(poke_dict.values())

# table.add_column("pokemon name", keys)
# table.add_column("type", values)


# print(table)

# day 17

# class User:
#     def __init__(self, userid, username): # this function is executed wnv new abj is created
#         self.id= userid
#         self.uname= username
#         self.followers=0
#         self.following=0

#     def follow(self, user):
#         user.followers+=1
#         self.following+=1


# user1= User(991, 'twuptea')
# user2= User(992, 'assiss')

# print(user1.uname)

# user1.follow(user2)

# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)


# user1.colour='black'

# print(user1.colour)  added attributes to the object

# constructors are used to initialize the objs


# day 17 quiz using oop

class Question:
    def __init__(self, que, ans):
        self.question = que
        self.answer = ans

question_data = [{'question': 'whats my name?', 'answer': 'trupti'},
                 {'question': 'there are 5 planets', 'answer': 'false'},
                 {'question': 'the sky is blue?', 'answer': 'true'}]

question_bank = []

for i in question_data:
    qtext = i['question']
    qans = i['answer']
    obj = Question(qtext, qans)
    question_bank.append(obj)

class Quizbrain:
    def __init__(self, que_list):
        self.que_no = 0       # dafault parameters
        self.que_list = que_list
        self.score = 0

    def Next_que(self):
        current_question = self.que_list[self.que_no]  # Update to get the current question based on que_no
        user_ans = input(f'Q. {self.que_no + 1} --> {current_question.question} (true or false): ')
        self.Check_ans(user_ans, current_question.answer)

    def Still_has_ques(self):
        return self.que_no < len(self.que_list)

    def Check_ans(self, user, correct):
        if user.lower() == correct.lower():
            print('Correct!!')
            self.score += 1
        else:
            print('Wrong')

        print(f'The correct answer is {correct}')
        print(f'Your score: {self.score}/{self.que_no + 1}')  # Update to show correct score
        print('\n')
        self.que_no += 1  # Increment question number after each question

quiz = Quizbrain(question_bank)
quiz.Next_que()

while quiz.Still_has_ques():
    quiz.Next_que()

print('You completed the game!!')
print(f'Final score: {quiz.score}/{quiz.que_no}')
