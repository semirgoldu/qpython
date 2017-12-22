import urllib2 
import time
from androidhelper import sl4a
import time as t
from bs4 import BeautifulSoup
import ssl 

try: 
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context 
droid = sl4a.Android()
def parseResult(soup):
    res = ""
    divClass = [
        ('div','_XWk'),
        ('div','cwos'),
        ('div','curtgt'),
        ('div','kpd-ans'),
        ('div','vk_ans'),
        ('div','_sdf'),
        ('div','kltat'),
        ('div','_oDd'),
        ('div','_xHd')
        
        
    
    ]
    for tag,className in divClass:
        
        if soup.findAll(tag,class_=className):
            if className == 'kltat':
                
                for q in soup.find_all(True,{"class":[className]}):
                    res += q.getText()+','
            else:
                res += soup.find(tag,class_=className).getText()+", "
            
        
    if res:
        return res
    else:
        return 'no result'
            
def getGoogleResult(query):
    query = query.replace(' ','+')
    url = "https://www.google.com/search?client=ms-android-blu&sourceid=chrome-mobile&ie=UTF-8&hl=en&q="+query+'&oq='+query
    opener = urllib2.build_opener() 
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; Life One X2 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36')] 
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        page = opener.open(url).read() 
    except:
        return 'no internet'
        return False
    soup = BeautifulSoup(page,'html.parser')
    
    #print soup.get_text().replace('&nbsp;','').encode('utf-8').strip()
    
    html = opener.open(url).read() 

    #print g.replace('&nbsp;','').encode('utf-8').strip()
    #print soup
    s = parseResult(soup)
    #print "-"*15+"Answer"+"-"*15
    return s
    #print s.replace('&nbsp;','').encode('utf-8').strip()
    #droid.ttsSpeak(s)