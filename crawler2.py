import requests
from bs4 import BeautifulSoup

url = 'https://ocjene.skole.hr'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

for link in soup.find_all('a'):
	email = link.get('href')
	# match and extract only the email pattern
	if email.startswith('mailto:'):
		print(email.replace('mailto:', ''))