import random

l=[]
for i in range(20000):
  l.append(random.randint(1,10000))

n=int(input("Enter a number to search: "))
flag=0
for i in range(len(l)):
  if n==l[i]:
    print(f"Found {n} in list")
    flag=1
    break
if flag==0:
  print("Could not find {n} in list.")
