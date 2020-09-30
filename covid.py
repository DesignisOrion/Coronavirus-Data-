

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.worldometers.info/coronavirus/'

r = requests.get(url)

s = BeautifulSoup(r.text, 'html.parser')

table = s.find('table', id='main_table_countries_today')


row_data = []

for row in table.find_all('tr')[9:25]:
    cols = row.find_all('td')[1:8]
    cols = [ele.text.strip() for ele in cols]
    row_data.append(cols)


df = pd.DataFrame(data=row_data, columns=[
    'Country', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases'])
