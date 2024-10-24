import random

l=[]
for i in range(10):
  l.append(random.randint(1,100))

print(l)
x=[]

while (len(l)>0):
  mini=l[0]
  for i in range(len(l)):
    if l[i]<mini:
      mini=l[i]
  x.append(mini)
  l.remove(mini)
print(l)
print(x)
