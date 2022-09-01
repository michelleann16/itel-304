a = float(input('7:'))
b = float(input('16:'))
c = float(input('23:'))

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c))** 0.5
print('The area of the triangle is %0.3f' %area)