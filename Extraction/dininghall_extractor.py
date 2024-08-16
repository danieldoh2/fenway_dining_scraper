from bs4 import BeautifulSoup
import requests

requ = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=34476&locationId=31992001&whereami=https://bufenway.sodexomyway.com/dining-near-me/campus-center-dining-room")

soup = BeautifulSoup(requ.text, 'html')

# items = soup.find_all('div', {'class': 'col-xs-9'})
# print(type(items))
foods = soup.find_all('a', {'href': '#'})
print(foods)