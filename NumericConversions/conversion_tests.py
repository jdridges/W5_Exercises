# Description:  This script tests various numeric
#               conversion techniques
#Author: Jacob R. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# int_a = (int(a))      #invalid literal for int() with base 10: ' 101.1 '
int_b = int(b)
# int_c = int(c)        #same error message as variable a.
#int_d = (int(d))       #same error messages as a and c

float_a = float(a)
float_b = float(b)
#float_c = float(c)     #could not convert string to float: '402 Stevens
#float_d = float(d)     #same error message as above

float_int_a = int(float(a))

print(a,b,c,d,int_b,float_a,float_b)

strip_a= str(a).strip()
print(strip_a)

strip_d = str(d).strip()
print(strip_a,strip_d)

print(a,type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(int_b, type(int_b))
print(float_a, type(float_a))
print(float_b, type(float_b))
print(float_int_a, type(float_int_a))

