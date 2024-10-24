num = int(input("Enter a number: "))
if num <0:
  print("Not Defined")
fact = 1
while (num > 0):
  fact = fact * num
  num = num - 1
print(fact)