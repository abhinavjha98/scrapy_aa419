import requests
from bs4 import BeautifulSoup

URL = 'https://db.aa419.org/fakebankslist.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

j=1
import pandas as pd
import requests
url_list = []
while(j<500):
  if j<500:
    URL = 'https://db.aa419.org/fakebankslist.php?start='+str(j)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tablerow = soup.find_all('tr', class_='ewTableRow')
    table_alt_row = soup.find_all('tr', class_='ewTableAltRow')
    
    tablerow = table_alt_row + tablerow
    for i in tablerow:
      for link in i.find_all('a', href=True):
        if "http" in link['href']:
          print(link['href'])
          url_list.append(link['href'])
    j+=20
    print(j)

df = pd.DataFrame(list(zip(url_list)),
               columns =['URL'])
df["Label"] = "Bad"
df.to_csv("Phishing_data.csv",index=False)
print(df)
