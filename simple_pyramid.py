""" python program for simple  pyramid  


* 
* * 
* * * 
* * * * 
* * * * *


"""
### get input from the user

row=int(input("enter the row"))


##logic for print the pattern
for i in range(row):
    for j in range(0,i+1):
        print("* " ,end="")
    print()