################################################################################
# Εφαρμογή υπολογισμου της τρεχουσας αξιας των κρυπτονομισματων
# Η εφαρμογη ζηταει απο το χρηστη ενα αρχειο λεξικου που περιεχει τον κωδικο
# και την ποσοτητα των κρυπτονομισματων
# URL: https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=EUR
################################################################################

import urllib.request
import urllib.error
import json

def get_file_content(fname):
# Διαβαζει τα περιεχομενα του αρχειου filename
# που περιεχει τον πινακα με τα κρυπτονομισματα του χρήστη
    try:
        with open(filename) as fp:
            mydict = json.load(fp)
        return mydict

    except FileNotFoundError:
        print('Το αρχείο {} δεν βρέθηκε'.format(filename))
        return -1

def get_coin_data(coins):
# Ανακτηση ισοτιμιων κρυπτονομισματων με το ευρω
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=EUR".format(coins)
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode()
            data = json.loads(html)
            return data

    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.readline())
        return -1
    except urllib.error.URLError as e:
        print(e)
        if hasattr(e, 'reason'):
            print('Αποτυχία σύνδεσης')
            print('Αιτία: ', e.reason)
        return -1


filename=input("Δώσε όνομα αρχείου: ")
if filename=='': exit

btcoins=get_file_content(filename)
if btcoins != -1:
    btcodes=""
    for k in btcoins.keys():
        btcodes+=k+","
    btcodes=btcodes[0:-1]

    times=get_coin_data(btcodes) # Τρεχουσες τιμες κρυπτονομισματων
    if times!=-1:
        print("=== Τρέχουσα αξία κρυπτονομισμάτων ===")
        print("="*38,"\n")
        total=0
        for k,v in btcoins.items():
            axia=times[k]["EUR"]*v
            total+=axia
            print("Έχετε {} μονάδες {} αξίας {:1.2f} ευρώ".format(v,k,axia))
        print("Συνολική αξία {:1.2f} ευρώ".format(total))
