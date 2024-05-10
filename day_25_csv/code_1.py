
# this is without importing the csv module
# with open ('weather_data.csv', 'r') as file:
#     data= file.readlines()

# for i in data:
#     name= i.strip()
#     print(name)

# using csv module--------------

# import csv

# with open ('weather_data.csv') as file:
#     data = csv.reader(file)  # an object is created here
    
#     temperature =[]
#     for j in data:
#         if j[1]!= 'temp':
#             temperature.append(int(j[1]))
#     print(temperature)
#     for i in data:
#         print(i)

# print(type(data))

# using pandas library-------

import pandas as pd

data= pd.read_csv('weather_data.csv')  #here data is alr converted into a tabular form and from here we can manipulate the data
print(data)
print('\n')
# print(type(data))
# data type is data frame- whole table

# the data is printed out in a table and properly formatted
# it takes the first row to be the heading of each column

# to print a single column of the table 
# print('\n')
# print(data['condition'])
# print(type(data['condition']))

# data type here is series-- its like a single column in your table
# can also convert our data into a dictionary and series into a list

# data_dict= data.to_dict()
# print(data_dict)

# condition_list= data['condition'].to_list()
# print(condition_list)

# calculating the average temperature---
temp_list= data['temp'].to_list()
avg= sum(temp_list)/len(temp_list)
print('\n')
# print(data['temp'])
# print(f'the average temperature is {avg}')

print(f'the mean is -- {data['temp'].mean()}\n')


# o find the maximum value:
print('\n')
print(f' the max value is {data['temp'].max()}\n')
print('\n')
# get ata in columns----
# print(data['condition'])
# OR print(data.condition)----- it takes the heading of the row as attribute

# how to get daya from a row of a data frame-------
# print(data[data.condition =='Sunny'])

# print the row of data with the max temperture----

# print(data[data.temp==data.temp.max()])

# the row which is/ the rows which are returned contain lots of unnecessary data 
# like if i want the temp of a particular day theres no need of the conditions to be displayed

# monday= data[data.day=='Monday']
# print(((9/5)*(monday.temp))+32)

# print('\n')

# create a data frame from scratch------
data_dict= {
    'students':['aashish', 'trupti','unnati'],
    'scores': [98, 99, 88]
}

data2= pd.DataFrame(data_dict)
print(data2)