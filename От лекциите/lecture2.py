# print('Hello World!')
# print(2+2)
# print(50-5*6)
# print((50-5)*6)
# print((50-5*6)/4)
# print(8/5)
# print(17/3)
# print(17//3)
# print(17 % 3)
# print(2**3)

# # 0=> ()
# # 1=> **
# # 2=> *,/,//,%
# # 3=> +,-

# width = 4
# height = 5
# print(width*height)

# width = int(input('a = '))
# height = int(input('b = '))
# print(width*height)

# width = float(input('a = '))
# height = float(input('b = '))
# area = width * height
# print('S = a*b = ', area)

# print(complex(2, 3))
# print(complex(4))

import random
import cmath

random.seed()
width = random.random()*10
height = random.random()*10
print('a=', width)
print('b=', height)

print(random.randrange(-5, 10, 3))  # -5,-5+3=-2, -2+3=1, 1+3=4, 4+3=7, 7+3=10
print(random.uniform(-5, 10))  # -5<=x<10

print(width, '   =>   ', round(width, 2))

print(cmath.sqrt(width))
