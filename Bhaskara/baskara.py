import sys

sys.path.append("../newton-raphson-sqrt")

from newton_raphson import square_root

a = 3
b = 4
c = 1

disc = b*b - 4*a*c
# validate the discriminator
if disc < 0:
  print("It does not exist solution!!!")
  exit
# validate quadratic equation
if a == 0:
  print("It not necessary Bhaskara for this equation")
  print("x: ",(float)-c/b)
  exit
    
x1 = (-b + square_root(disc))/(2*a)
x2 = (-b - square_root(disc))/(2*a)

#print(square_root(27))

print "x1: %.2f"%x1)
print("x2: %.2f"%x2)

