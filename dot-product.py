import random

x=[]
y=[]

for i in range(10):
  x.append(random.randint(1,100))
  y.append(random.randint(1,100))

print(x)
print(y)

if len(x)!=len(y):
  raise ValueError("Vectors must be of the same length")

dot_product=0

for i in range(len(x)):
  val=x[i]*y[i]
  dot_product+=val

print(dot_product)