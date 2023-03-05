a = (14,21,66,14,33,38,29,37,154,12,191,26,35)
even,odd= 0,0
 
for i in a:

   if (i%2==0):
             even +=1
   else:
             odd +=1
print("no. of even numbers in the series = ",even)
print("no. of odd numbers in the series =", odd)