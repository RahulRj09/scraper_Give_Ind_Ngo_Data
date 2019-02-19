import requests
from bs4 import BeautifulSoup as bs
import html5lib
from pprint import pprint
import json
import pathlib
import os
from random import randint
from time import sleep


url = "https://www.giveindia.org/certified-indian-ngos"
data = requests.get(url).text
data = bs(data, 'html5lib')
tbody = data.find('tbody')
ngolist = []

for tr in tbody.find_all('tr'):
	l = []
	data = {}
	i = 0
	for td in tr.find_all('td'):
		
		td = td.text
		td = td.split("<td>")
		l +=td
		i +=1
		if i == 3:
			data['name'] = l[0]
			data['work'] = l[1]
			data['state'] = l[2]	
			break
		ngolist.append(data)

ngobystate = {}
for i  in range(len(ngolist)):
	if ngolist[i]['state'] in ngobystate:
		ngobystate[ngolist[i]['state']].append(ngolist[i]) 
	else:
		ngobystate[ngolist[i]['state']] = [ngolist[i]]

pprint(ngobystate)
