from bs4 import BeautifulSoup
import requests
import re
import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='machin')
user_brand = input()
a = 0
for i in range(2,100):  
  if a == 20:
    break
  cursor = cnx.cursor()
  page = requests.get("https://www.truecar.com/used-cars-for-sale/listings/?page={}".format(i))
  soup = BeautifulSoup(page.content, "html.parser")
  cars_elements = soup.find_all('div', {'data-test':'cardContent'}) 
  for element in cars_elements:
    cartitle = (element.find('div',{'data-test':'vehicleCardYearMakeModel'}).text.strip())
    brand = (re.findall(r'\w*[A-Z]\w*', cartitle)[0])  
    if brand == user_brand: 
      a += 1   
      price = float(element.find('div',{ 'data-test':"vehicleListingPriceAmount"}).text.replace('$','').replace(',','.'))
      miles = float(element.find('div', {'data-test':"vehicleMileage"}).text.replace(' miles','').replace(',','.'))
      cursor.execute("insert into item(price,miles) values('{}','{}')".format(price,miles))
  
cnx.commit()
cnx.close()