""" python program  for right angle pyramid   


         * 
       * * 
     * * * 
   * * * * 
  * * * * *
  
  """
  
  ## get input from the user

row=int(input("enter the row"))
k=2*row-2     # It is used for number of spaces

##logic for print the pattern
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k=k-2    # decrement k value after each iteration  
    for j in range(0,i+1):
        print("* ",end="")   ###print pattern
        
        
    print("")
         