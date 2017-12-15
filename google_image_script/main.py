from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json
import ssl
from androidhelper import sl4a
try: 
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context
droid = sl4a.Android()
def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

query = raw_input("Query Input: \n")
image_type="Pic"
query= query.split()
query='+'.join(query)
url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
print url
#add the directory for your image here
DIR="/sdcard/resource/google/images"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


img=[]
# contains the link for large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    img.append((link,Type))
    if len(img) > 3:
    	break

print  "getting" , len(img),"images"
#create main directory if it doesn't exist
if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])
#create directory for query if does not exist
if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( img):
    try:
        req = urllib2.Request(img, headers={'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()
        #check existing images in directory and increment counter
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print cntr
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
        
    except Exception as e:
        print "could not load : "+img
        print e