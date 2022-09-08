from bs4 import BeautifulSoup
import requests
page = requests.get("https://divar.ir/s/tehran/")
soup = BeautifulSoup(page.content, "html.parser") 
all_ads = soup.find_all('div', {'class' : 'kt-post-card__body'}) 
for ads in all_ads:
  if 'توافقی' in ads.get_text():        
    title_ads = ads.find('div',{'class' : 'kt-post-card__title'})    
    print(title_ads.text.strip())