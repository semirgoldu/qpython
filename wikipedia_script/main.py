import wikipedia as w
from androidhelper import sl4a
droid = sl4a.Android()
run = True
while run:
	query = raw_input("Query: ")
	try:
	    res= w.summary(query,sentences=3)
	except:
	    res = "no result"
	print res.encode("utf-8"). strip()