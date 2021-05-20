""" python program  for two pyramid in single pattern  
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
* * * * * * *  
* * * * * * *  
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*



"""
### get input from the user

row=int(input("enter the row"))


##logic for print pattern
for i in range(row):
    for j in range(0,i+1):
        print("* " ,end="")
    print()
    
    
###logic for second pattern


for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("* " ,end="")
    print()