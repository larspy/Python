#! /usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
def systeminfo():
	os.system("systeminfo > info.txt")
	os.system("netstat -a > ipinfo.txt")
	os.system("ipconfig /all > ipconfig.txt")
def findpublicip():
	r = requests.get("https://www.whatismyip.com/what-is-my-public-ip-address/")
	soup = BeautifulSoup(r.content,"html5lib")
	a = soup.find_all("span")
	for i in a:
		file = open("public.txt","a")
		file.write(str(i)+"\n")
		file.close()
findpublicip()
