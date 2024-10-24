# Write a Python code using functions which calculates the number of upper case, lower case letters, total number of characters ad number of words.

sentence=input("Enter the sentence: ")
def ucl(s):
  upper=0
  for c in s:
    if (c.isupper()):
      upper+=1
  return(upper)

def lcl(s):
  lower=0
  for c in s:
    if (c.islower()):
      lower+=1
  return(lower)

def total(s):
  chars = 0
  for c in s:
    chars +=1
  return chars

def words(s):
  words=1
  for c in s:
    if(c == " "):
      words+=1
  return words

print(f"{ucl(sentence)} {lcl(sentence)} {total(sentence)} {words(sentence)}", end="")