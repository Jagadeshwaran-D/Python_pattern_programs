"""  python program  for  number pattern  

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  
"""
""

### get input from the user

row=int(input("enter the row"))


##logic for print the pattern
for i in range(row+1):
    for j in range(i):
        print(i ,end="")
    print()


