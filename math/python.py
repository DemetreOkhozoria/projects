#user chooses numbers and signs
a = input("Choose : - or + or /")
b =int(input("Choose a number"))
c =int(input("Choose a number"))
#cheching what they entered
if a == "-": print(b-c)
elif a == "+": print(b+c)
elif a == "/": print(b/c)
else:
    print("Wrong sorry")
