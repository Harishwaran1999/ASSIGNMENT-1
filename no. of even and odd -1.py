series= (1,2,5,56,897,4,54,55,14,21,66)
even = 0
odd = 0
for i in series:

   if (i%2==0):
             even= even +1
   else:
             odd = odd +1
print("no. of even numbers in the series = ",even)
print("no. of odd numbers in the series =", odd)