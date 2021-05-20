"""  python program for inverted number pyramid """

### get input from the user

row=int(input("enter the row"))


##logic for print the pattern
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(i ,end="")
    print()