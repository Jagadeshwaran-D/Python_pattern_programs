""" python program  for  Hour glass pattern


    * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * *
  
  
  """
  
     ## get input from the user

row=int(input("enter the row"))

k=row-2     # It is used for number of spaces

##logic for print downward triangle pattern
for i in range(row,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1    # decrement k value after each iteration  
    for j in range(0,i+1):
        print("* ",end=" ")   ###print pattern
        
        
    print()
    
    
k=2*row-2     # It is used for number of spaces

##logic for print upward triangle pattern
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k=k-1    # decrement k value after each iteration  
    for j in range(0,i+1):
        print("* ",end=" ")   ###print pattern
        
        
    print()
    