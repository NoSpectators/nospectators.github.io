# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:33:14 2016

@author: John
"""

import csv 
from urllib2 import urlopen
from bs4 import BeautifulSoup
#schools 1-100
html=urlopen("http://www.greatschools.org/washington-dc/washington/schools/?st=charter")
bsObj =BeautifulSoup(html.read())
#schoolsList=bsObj.findAll("a", {"href":re.compile("http://www.greatschools.org/washington-dc/washington/")})

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)
    
school_info=[]
js_code = bsObj.find_all("script")[1].text
js_code_new = remove_non_ascii_1(js_code)
js_code_new = str(js_code_new)
js_code_new = js_code_new.split(",")
#print js_code_new
print len(js_code_new)
for item in js_code_new:
    if '"name":' in item:
        #print item
        #print item[8:]
        school_name=item[8:]
        #school_info.append(school_name)
        pass
    if '"street":' in item:
        #print item
        street_address = item[9:]
        
    if '"zipcode":' in item:
        zipcode = item[10:]
        school_info.append([school_name,street_address,zipcode])
#school_info[0][0]="'KIPP DC PCS: KEY Academy'"

school_info[0][0] = school_info[0][0][71:]



#schools 101-115
html2 = urlopen("http://www.greatschools.org/washington-dc/washington/schools/?page=5&st=charter")
bsObj2 = BeautifulSoup(html2.read())
schools115=[]
js_code2 = bsObj2.find_all("script")[1].text
js_code_new2 = remove_non_ascii_1(js_code2)
js_code_new2 = str(js_code_new2)
js_code_new2 = js_code_new2.split(",")
#print js_code_new
print len(js_code_new2)
for item in js_code_new2:
    #print item
    if '"name":' in item:
        #print item
        #print item[8:]
        school_name=item[8:]
        #school_info.append(school_name)
        pass
    if '"street":' in item:
        #print item
        street_address = item[9:]
        
    if '"zipcode":' in item:
        zipcode = item[10:]
        schools115.append([school_name,street_address,zipcode])
#school_info[0][0]="'KIPP DC PCS: KEY Academy'"



schools_info2 =[]
for item in school_info:
    school = item[0]
    school = school[1:-1]
    street = item[1]
    street = street[1:-1]
    zipcode = item[2]
    zipcode = zipcode[1:-1]
    schools_info2.append((school, street, zipcode))
    
schools101_115=[]
for item in range(86,len(schools115)):
    schools101_115.append(schools115[item])
#print schools101_115
    
schools101_115_2 = []
for item in schools101_115:
    school = item[0]
    school = school[1:-1]
    street = item[1]
    street = street[1:-1]
    zipcode = item[2]
    zipcode = zipcode[1:-1]
    schools101_115_2.append((school, street, zipcode))
    

with open('charters.csv','wb') as fp:
    a = csv.writer(fp, delimiter=",")
    a.writerow(['school_name','street_address','zipcode'])
    a.writerows(schools_info2)
    a.writerows(schools101_115_2)
    
