import requests
import bs4
import re
 
url = 'https://' + input('Give site URL: ')

try:
    r = requests.get(url)
    print(r.text)
    soup = bs4.BeautifulSoup(r.text, "html.parser")

except Exception as err:
    print("Error accessing url:", url)
    print(err)

else:
    for anchor in soup.find_all('a'):
        print(anchor.get('href'))

    for e in soup.find_all(re.compile("engineer"), re.IGNORECASE):
        print(e)