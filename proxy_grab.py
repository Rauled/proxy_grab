import requests
from bs4 import BeautifulSoup as bs
import itertools
import re
import base64
 
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0(X11;Linux x86_64...)Geco/20100101 Firefox/60.0'}
page = 1
base_url = 'http://proxy-list.org/russian/index.php?p=' + (format(page))


def proxy_parse(base_url, headers):
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        lis = soup.find_all("li", class_={'proxy'})
        his = ''.join(str(lis))
        x = his.split("'")
        x = x[1::2]
        for dec in x:
            unic = base64.b64decode(dec)
            print(unic)
            with open("proxy.txt", "a+") as file:  
                file.write(str(unic.decode()))
                file.write('\n')


while page != 10:
    proxy_parse(base_url, headers)
    page += 1
