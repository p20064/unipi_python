################################################################################
# Η εφαρμογη ζηταει απο το χρήστη ενα αρχειο ASCII και αφου κρατησει μονο τους
# ASCII χαρακτηρες κεφαλαιων και πεζων γραμματων στη συνεχεια τους μετατρεπει
# στους αντιστοιχους ASCII δεκαδικους κωδικους.
# Μετατρεπει στον αντιστοιχο ASCII code μονο τους χαρακτηρες με μονό ASCII code
# Καταμετρα την εμφανιση καθε χαρακτηρα απο αυτους και εμφανιζει
# στατιστικα εμφανισης
################################################################################

import string

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
# Αφαιρει απο το κειμενο οσους χαρακτηρες δεν ανηκουν στα ascii letters
    new_text=""
    for letter in keimeno:
        if (letter in string.ascii_letters):
            new_text += letter
    return new_text

filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit
text=get_file_content(filename)
if (text!=-1):
    text = clear_keimeno(text)

    C=[]
    # Δημιουργει λιστα με τους μονους χαρακτηρες προς καταμετρηση
    for letter in text:
        code = ord(letter) # character ascii code
        if ((letter not in C) and (code%2==1)): C.append(letter)
    C.sort()

    chars={}
    # Δημιουργια και μηδενισμος του λεξικου chars που περιεχει τη συνολικη
    # εμφανιση των μονων χαρακτηρων στο κειμενο
    for letter in C:
        chars[ord(letter)]=0

    total = 0
    # Καταμετρηση εμφανισης χαρακτηρων
    for letter in text:
        code = ord(letter)
        if (code%2==1):
            chars[code] += 1
            total += 1

    # Υπολογισμος και εμφανιση ποσοστων
    for c,v in chars.items():
        pososto = int(round((v/total*100)+0.5, 0))
        print("{} \t ascii code({:d}):{}({})".format(chr(c), c, "*"*pososto, v))
