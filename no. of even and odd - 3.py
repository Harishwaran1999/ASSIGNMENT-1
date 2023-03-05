s1 = (14,21,66,14,33,38,29,37,154,12,191,26,35)
s2 = (11,22,33,44,55,66,77,88,99,222)
even,odd= 0,0
even_count,odd_count = 0,0
 
for i in s1:

   if (i%2==0):
             even +=1
   else:
             odd +=1

for x in s2:

   if (x%2==0):
             even_count +=1
   else:
             odd_count +=1
print("no. of even numbers in the series 1 = ",even)
print("no. of odd numbers in the series 1 =", odd)
 

print("no. of even numbers in series 2 = ",even_count)
print("no. of odd numbers in series 2 =", odd_count)