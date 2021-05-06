from bs4 import BeautifulSoup
import requests
import pandas as pd

URL ='https://en.wikipedia.org/wiki/Rugby_World_Cup_all-time_table'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

table = soup.find('table', {'class':'wikitable sortable'}).tbody

rows = table.find_all('tr')
columns = [i.text.replace('\n', '') for i in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(1,len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n','').replace('\xa0','').replace('—','0').replace('−', '')  for td in tds]
    
    df = df.append(pd.Series(values, index=columns), ignore_index=True)

df.to_csv(r'C:\Users\lacar\DQ Projects\Rugby DataVis' + '\\alltimeRWCrecords1.csv', index=False)
