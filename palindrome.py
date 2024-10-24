num = int(input("Enter a number to reverse: "))
absNum = abs(num)
rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
  r = absNum % 10
  absNum = absNum // 10
  rev = rev * 10 + r
if (num == rev or num == (rev - 2 * rev)):
  print("This is a Palindrome")
else:
  print("This is NOT a Palindrome")