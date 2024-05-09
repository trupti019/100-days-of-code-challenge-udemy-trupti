
# use open function to read the content of the file

f= open("sample.txt", "r") # opens the file in read mode
data = f.read()             # reads its contents
print(data)                 #print its contents
f.close()                   #close the file

# other functions to read a file-- f.readline()-- reads a single line

# modes of opening a file:
'''
r- reading
w- writing
a- append
+ - updating

rb will open for read in binary mode
rt will open for read in text mode
'''


# new= open('another.txt', 'a')
# new.write('aashish is my good boy')
# f.close()

# with statement-- contex manager
'''this is the best way to open and close a file automatically
syntax:
with open ('filename) as f:
    f.read()
    '''

with open('another.txt', mode='r') as boo:
    a= boo.read()

print(a)



# absolute file path and relative file path


