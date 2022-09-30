
import pandas as pd

import os

import requests 
from bs4 import BeautifulSoup
url = "https://www.emag.ro/laptopuri/c"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
 

data_fetch = []

item_name = soup.find_all("a",class_="card-v2-title semibold mrg-btm-xxs js-product-url")
item_text = [n.get_text() for n in item_name]

price_elements = soup.find_all("p",class_="product-new-price")
prices_text = [p.get_text() for p in price_elements]

stock_element = soup.find_all("div",class_="card-estimate-placeholder")
in_stock = [p.get_text() for p in stock_element]



name = item_name
price = prices_text
stock = in_stock
     
# dictionary of lists  
dict = {'Name' : item_text,'Price': price,'In Stoc':stock}  

#this is needed only if len of values are not the same
#df = pd.DataFrame.from_dict(dict, orient='index')
#df = df.transpose()

       
df = pd.DataFrame(dict) #working
    
# saving the dataframe 
df.to_csv('emag_prices.csv') 
file_path = os.getcwd()

print('Get current working directory : ', os.getcwd())

print('File [emag_prices.csv] created on: [',file_path,']')




