filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit

try:
    with open(filename, "r") as f:
        text = f.read()

    text=text[::-1]

    new_text=''
    for letter in text:
        new_text+=chr(128-ord(letter))

    print(new_text + "\n")

except FileNotFoundError:
    print('Το αρχείο {} δεν βρέθηκε'.format(filename))
    exit
