import requests
from bs4 import BeautifulSoup
import pandas as pd

response=requests.get('https://books.toscrape.com/')
print(response.status_code)
if response.status_code == 200:
    print('Successfully done')
else:
    print('Try another way')

print(response.text[:500])
soup=BeautifulSoup(response.text,'lxml')
print(soup.prettify())

products=soup.find_all('article',class_='product_pod')
data=[]

for i in products:
    title=i.h3.a['title']
    price=i.find('p',class_='price_color').text
    availability=i.find('p',class_='instock availability').text.strip()
    print(title , price , availability)
    data.append([title,price,availability])

data1=pd.DataFrame(data, columns=['Title','Price','Availability'])
print(data1)