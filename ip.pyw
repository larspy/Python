#! /usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
def findpublicip():
	r = requests.get("https://www.whatismyip.com/what-is-my-public-ip-address/")
	soup = BeautifulSoup(r.content,"html5lib")
	a = soup.find_all("span")
	save_question = input("Save File [Y,N] ? ")
	if save_question == "y" or "Y":
		file_name = input("\t\t\tFile Name: ")
		for i in a:
		file = open(file_name,"a")
		file.write(str(i)+"\n")
		file.close()
	
findpublicip()
