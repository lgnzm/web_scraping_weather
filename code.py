# Import libraries

from bs4 import BeautifulSoup
import requests
import os
import csv
import datetime
import json
import calendar
from datetime import date

#create a csv file to save the data collected
csv_file=open('weathe.csv', 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['hour','weather_condition','temperature','wind','humidity','pressure'])

#define the link
link = requests.get("https://en.tutiempo.net/records/lfpo/1-june-2021.html")

#make soup
soup = BeautifulSoup(link.text,"html.parser")
print(soup.prettify()[0:1000])

#find the first table
soup.find_all('table')[1]

#find all the rows of the first table
all_rows = soup.find_all('table')[1].find_all('tr')
print(all_rows)

#print all the rows' text 
for tag in all_rows:
    print(tag.get_text())

#The range(2, len(all_rows), 2) generates a sequence starting from index 2 
# and incrementing by 2 until it reaches the length of all_rows
#this prints all rows but removes the empty rows
for line in range (2, len(all_rows), 2):
    print(all_rows[line].text)

#write the data in the rows in a csv file
for line in range(2,len(all_rows),2):
    hour = all_rows[line].find_all('td')[0].text
    weather_condition =all_rows[line].find_all('td')[1].text
    temperature = all_rows[line].find_all('td')[2].text
    wind = all_rows[line].find_all('td')[3].text
    humidity= all_rows[line].find_all('td')[4].text
    pressure = all_rows[line].find_all('td')[5].text
    csv_writer.writerow([hour,weather_condition,temperature,wind,humidity,pressure])
csv_file.close()