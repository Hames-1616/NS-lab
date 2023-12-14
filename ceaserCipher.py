message = input("Enter the message : ")
key = int(input("Enter the key : "))
cipher=""
for i in message :
    print(ord(i))
    if i.isupper():
        value = (ord(i) + key - 65 ) % 26 + 65
        cipher += chr(value)
    else :
        value = (ord(i) + key - 97 ) % 26 + 97
        cipher += chr(value)
    
print(cipher)