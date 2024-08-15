from bs4 import BeautifulSoup
import requests

requ = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=34476&locationId=31992001&whereami=https://bufenway.sodexomyway.com/dining-near-me/campus-center-dining-room")

print(type(requ), (requ))
print('fl')