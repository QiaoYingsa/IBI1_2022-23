i=1
n=2 #define the original variable
while n<100: #when rabbits are less than 100
   print(n)  #print the rabbits this generation borns 
   n=2*n     #calculate the next generation
   i=i+1     #add to the generation
# The final n is no less than 100. 
# If the number is 100, the next generation is suitable. 
# If the number is above 100, this generation is suitable.
if n==100:
   i=i+1
   print("The number of generations required to exceed 100 rabbits is " + str(i))
else:
   print("The number of generations required to exceed 100 rabbits is " + str(i))

   