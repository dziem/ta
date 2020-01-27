import requests

from selenium import webdriver
import time

import pandas as pd
import numpy as np
import csv
import os

driver = webdriver.Chrome(executable_path=r"C:\Users\D'ziem\Downloads\chromedriver.exe")
link = "https://forum.femaledaily.com/showthread.php?11862-Dry-Shampoo"
driver.get(link)
'''
weblinks = driver.find_elements_by_class_name('title')
#print(weblinks)
pagelinks = []
#post = []
for link in weblinks[4:100]:
	pagelinks.append(link.get_attribute('href'))
#print(pagelinks)
'''
i = 0
file = open('raw.txt','w', encoding='utf-8') 
for z in range(1,29):
    if z > 1:
        nextPage = link + '/page' + str(z)
        driver.get(nextPage)
    posts = driver.find_elements_by_class_name('postcontent')
    for q in posts:
        i += 1
        #post.append(q.text)
        file.write('\n')
        file.write('-----')
        file.write(str(i))
        file.write('-----')
        file.write('\n')
        file.write(q.text)
driver.close()
file.close() 
'''
with open('post.csv', 'w', newline='', encoding='utf-8') as csv_file:
	writer = csv.writer(csv_file, delimiter=';')
	for row in post:
		writer.writerow([row,])
'''