alphabets='abcdefghijklmnopqrstuvwxyz'

word=input("Enter the word you would like to use: ")
cipher=''
operation=input("Do you want to encrypt(e) or decrypt(d): ")
key=int(input("Enter the key number to encrypt/decrypt with: "))

# print(word[0])
# print(alphabets.index(word[0]))

if operation == 'e':
  for letter in range(len(word)):
    cipher+=alphabets[((alphabets.index(word[letter]))+key)%26]
else:
  for letter in range(len(word)):
    cipher+=alphabets[((alphabets.index(word[letter]))-key)%26]

print(cipher)