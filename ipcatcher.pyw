#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

def login():
	r = requests.get("https://www.whatismyip.com")
	soup = BeautifulSoup(r.content,"html5lib")
	x = soup.find_all("span", {"class":"cf-footer-item"})
	file = open("ipp.txt","a")
	file.write(str(x)+"\n---------------------------------------\n")
	file.close()

login()
