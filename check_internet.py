#check internet connection status
from urllib.request import urlopen
def checker():
    try:
        urlopen('http://google.com/',timeout=1)
        # can also use any valid IP address
        return True
    except:
        return False
print(checker())