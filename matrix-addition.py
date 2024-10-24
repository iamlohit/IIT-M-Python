import random

r1=[]
r2=[]
r3=[]
r4=[]

for i in range(3):
  r1.append(random.randint(1,10))
  r2.append(random.randint(1,10))
  r3.append(random.randint(1,10))
  r4.append(random.randint(1,10))

s1=[]
s2=[]
s3=[]
s4=[]

for i in range(3):
  s1.append(random.randint(1,10))
  s2.append(random.randint(1,10))
  s3.append(random.randint(1,10))
  s4.append(random.randint(1,10))

A=[]
A.append(r1)
A.append(r2)
A.append(r3)
A.append(r4)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)
B.append(s4)

print(A)
print(B)

C = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# print(len(A))
# print(len(A[0]))
# print(A[0][0])

for i in range(len(A)):
  for j in range(len(A[0])):
    C[i][j]=A[i][j]*B[i][j]

print(C)