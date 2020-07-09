import re
import time
import requests
import openpyxl
from openpyxl import Workbook
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

job_domain = "python"
loaction = "bangalore"
url = 'https://www.naukri.com/%s-jobs-in-%s?k=%s&l=%s' % (job_domain , loaction , job_domain , loaction)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

src = driver.page_source
soup = BeautifulSoup(src , 'html.parser')
results = soup.find('section' , class_ = 'listContainer fleft')

wb = Workbook()
sheet =  wb.active
sheet.title = "JOBS"
col = 4
l = ['Company' , 'JobTitle' , 'Salary' , 'Skills Required']
for i in range(1 , col+1):
    c = sheet.cell(row = 1, column = i)
    c.value = l[i-1]
wb.save("C:\\Users\\Ruchi\\demo.xlsx")

j_title = results.find_all('a' , class_ = 'title fw500 ellipsis')
job_title = []
for job in list(j_title):
    job_title.append(job.text)

comp_name = results.find_all('a' , class_ = 'subTitle ellipsis fleft')
comp_title = []
for nam in list(comp_name):
    comp_title.append(nam.text)

salaries = results.find_all('span' , class_ = 'ellipsis fleft fs12 lh16')
sals = []
for sal in list(salaries):
    sals.append(sal.text)

sheet =  wb.active
row = 20
col = 4
for j in range(1, col+1):
    oo = 0
    for i in range(2, row+2):
        c1 = sheet.cell(row = i, column = j)
        if j==1:
            c1.value = comp_title[oo]
            oo+=1
        elif j==2:
            c1.value = job_title[oo]
            oo+=1
        else:
            c1.value = sals[oo+1]
            oo+=3

skills = results.find_all('ul' , class_ = 'tags has-description')
skls = []
#print(skills , '\n\n')
for index  , skill in enumerate(skills):
    nn = skill.find_all('li' , class_ = 'fleft fs12 grey-text lh16 dot')
    for jj in nn:
        skls.append(jj.text)
    print(skls , '\n')
    c2 = sheet.cell(row = index+2 , column = 4)
    c2.value = str(skls)
    skls = []
wb.save("C:\\Users\\Ruchi\\demo.xlsx")