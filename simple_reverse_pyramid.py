""" python program for simple reverse pyramid  

* * * * *
* * * *
* * *
* *
*

"""

### get input from the user

row=int(input("enter the row"))


##logic for print the pattern
for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("* " ,end="")
    print()