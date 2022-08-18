#method-1
r=float(input('enter the radius of the circle:'))
sqr=r*r
pi=3.141592653589793
area=pi*sqr
print('the area of the circle with radius',r,'is:',area)


#method-2
import math as m
r=float(input('enter the radius of the circle:'))
sqr=r*r
area=m.pi*sqr
print('the area of the circle with radius',r,'is:',area)
