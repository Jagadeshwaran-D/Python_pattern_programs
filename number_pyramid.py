"""  python program  for number pyramid   


1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5


"""


### get input from the user

row=int(input("enter the row"))


##logic for print the pattern
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j ,end="")
    print()