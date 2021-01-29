def clear_keimeno(keimeno):
    new_text=""
    for letter in keimeno:
        if (0<=ord(letter)<=128):
            new_text += letter
    return new_text

filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit

try:
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()

    text=clear_keimeno(text)
    text=text[::-1]

    new_text=''
    for letter in text:
        new_text+=chr(128-ord(letter))

    print(new_text + "\n")

except FileNotFoundError:
    print('Το αρχείο {} δεν βρέθηκε'.format(filename))
    exit
