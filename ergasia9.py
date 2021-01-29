import string

def clear_keimeno(keimeno):
    new_text=""
    for letter in keimeno:
        if (letter in string.ascii_letters):
            new_text += letter
    return new_text

filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit

try:
    with open(filename, "r") as f:
        text = f.read()

    text = clear_keimeno(text)
    C=[]
    for letter in text:
        code = ord(letter) # character ascii code
        if ((letter not in C) and (code%2==1))): C.append(letter)
    C.sort()

    chars={}
    for letter in C:
        chars[ord(letter)]=0

    total = 0.0
    for letter in text:
        code = ord(letter)
        if (code%2==1):
            chars[code] += 1
            total += 1

    for c,v in chars.items():
        pososto = int(round((v/total*100)+0.5, 0))
        print("{} \t ascii code({:d}):{}({})".format(chr(c), c, "*"*pososto, v))

except FileNotFoundError:
    print('Το αρχείο {} δεν βρέθηκε'.format(filename))
    exit
