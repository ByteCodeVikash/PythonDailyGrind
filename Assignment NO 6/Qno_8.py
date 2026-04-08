"""
8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
"""

a=intput("Enter a value: ")
b=intput("Enter b value: ")
c=intput("Enter c value: ")

d=b**b-4*a*c

if d>0:
   print("Real or distinct roots.")
elif d==0:
   print("Real or equal roots.")
else:
   print("imaginary roots.")      