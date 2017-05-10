# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil


url = "https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq=1494419964"

for i in range(100):
	print("Getting page for "+str(i))
	while(True):
		try:
			response = requests.get(url, stream=True)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
	with open('Stock/'+str(i)+'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response