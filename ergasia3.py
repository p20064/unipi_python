#################################################################################
# Εφαρμογή για τη δημιουργία στατιστικών για την  πρώτη κλήρωση της ημέρας,
# για τον τρέχοντα μήνα για το ΚΙΝΟ. Το παιχνίδι αλλάζει αν το ορίσουμε
# στη μεταβλητή gameID
# URLs:
# "https://api.opap.gr/draws/v3.0/{gameId}/draw-date/{fromDate}/{toDate}/draw-id"
# "https://api.opap.gr/draws/v3.0/{gameId}/{drawId}"
#################################################################################


import urllib.request
import urllib.error
import json
from datetime import date

nums={}

def get_web_content(url):
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


gameID=1100
cDate=date.today() # Current date
base_url="https://api.opap.gr/draws/v3.0/{:04d}/draw-date/".format(gameID)
yearMonth="{:04d}-{:02d}-".format(cDate.year, cDate.month) # Current month and year

message = "Στατιστικά κληρώσεων ΟΠΑΠ για το πρώτο παιχνίδι ΚΙΝΟ της ημέρας στην περίοδο: {:d}-{:d}".format(cDate.month, cDate.year)
print(message)
print("="*len(message))

for i in range(cDate.day):
    # Δημιουργία URL
    url=base_url + yearMonth + "{:02d}/".format(i + 1) + yearMonth + "{:02d}/draw-id".format(i + 1)
    # Εύρεση draw-id για τις ημερήσιες κληρώσεις
    draws = get_web_content(url)

    if draws != -1: # Αν επιστρέψει κληρώσεις
        draws.sort()
        # Δημιουργία URL πρώτης ημερήσιας κληρωσης
        durl="https://api.opap.gr/draws/v3.0/{:04d}/{}".format(gameID, draws[0])
        data=get_web_content(durl)

        if data!=-1: # Αν επιστρέψει στοιχεία για την κλήρωση
            # Δημιουργία λίστας με τους αριθμούς που κερδίζουν
            L=data['winningNumbers']['list']
            L.sort()

            for item in L:
                if item in nums:
                    nums[item]+=1
                else:
                    nums[item]=1

if len(nums) > 0:
    maxFores = max(nums.values())
    for i in range(1, maxFores+1):
        print("Από {} φορές: ".format(i))
        for k,v in nums.items():
            if v == i:
                print(k, end=" ")
        print("\n")
