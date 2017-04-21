#!/usr/bin/python  
# -*- coding: utf-8 -*-
import requests 
from lxml import html 
import sys
import os
from urllib.parse import urljoin

#proxy = 'xxxx:xx'
#os.environ['http_proxy'] = proxy 
#os.environ['HTTP_PROXY'] = proxy
#os.environ['https_proxy'] = proxy
#os.environ['HTTPS_PROXY'] = proxy

url='http://www.backchina.com/forum/20170413/info-1460447-1-1.html'  
folder='C:\Private\Analysis\python\mine\download_pic'

response = requests.get(url)
parsed_body = html.fromstring(response.text)

# Grab links to all images
images = parsed_body.xpath("//img/@src[contains(., '.jpg')]")  ## please change the type of images
if not images:  
    sys.exit("Found No Images")

# Convert any relative urls to absolute urls
images = [urljoin(response.url, url) for url in images]  
print ('Found %s images' % len(images))

index=1
for url in images[0:100]:## 100 will scrape 100 pictures
	try:
		r = requests.get(url)
		#f = open(folder + '/%s' % url.split('/')[-1], 'wb')
		f = open(folder + '/%s' % str(index)+'.jpg', 'wb')
		f.write(r.content)
		f.close()
	except:
		continue
	index+=1
