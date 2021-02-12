#########################################################
# Η εφαρμογη ζηταει απο το χρήστη ενα αρχειο ASCII
# Μετατρεπει τον ASII Code για καθε χαρακτηρα
# στο συμπληρωμα του ως προς 128 (τον κατοπτρικο του)
# Αντιστρεφει το κειμενο και εμφανιζει τους κατοπτρικους
# χαρακτηρες με αναποδη σειρα
#########################################################
def get_file_content(fname):
# Διαβαζει τα περιεχομενα του αρχειου fname
    try:
        with open(fname, "r", encoding = "utf-8") as f:
            text = f.read()
        return text

    except FileNotFoundError:
        print('Το αρχείο {} δεν βρέθηκε'.format(fname))
        return -1

def clear_keimeno(keimeno):
    # Αφαιρει ολους τους χαρακτηρες με ASCII code
    # που δεν ειναι αναμεσα στο 0 και το 255
    new_text=""
    for letter in keimeno:
        if (0<=ord(letter)<=255):
            new_text += letter
    return new_text

def katoptriko(keimeno):
    # Μετατρεπει καθε ASCII code στον κατοπτρικο του
    new_text=""
    for letter in keimeno:
        new_text+=chr(128-ord(letter))
    return new_text

filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit

text=get_file_content(filename)

if (text!=-1):
    text=clear_keimeno(text)
    # Αντιστροφη του κειμενου
    text=text[::-1]
    # Μετατροπη καθε χαρακτηρα στον κατοπτρικο
    text=katoptriko(text)

    print(text + "\n")
