# oop in python

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

from prettytable import PrettyTable
table= PrettyTable()
poke_dict={}
num=int(input('how many pokemons would u like to enter: '))
for i in range(0,num):
    poke_type= input('enter pokemon and its type (pokemon: type) :')
    poke, type= poke_type.split(":")
    poke_dict[poke.strip()]= type.strip()

print(poke_dict)

keys= list(poke_dict.keys())
values= list(poke_dict.values())

table.add_column("pokemon name", keys)
table.add_column("type", values)


print(table)