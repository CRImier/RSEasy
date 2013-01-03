## -*- coding: utf-8 -*-
import urllib2
import re

def getdirs(tr_id, num_tr, num_week):
  # RS specific - manipulating with intervals
	interval = lambda x: (((x - 1) / 10) * 10) + 1
	if tr_id == "tram" or tr_id == "night_bus": #no interval value needed for tram and night_bus
		interval_c = ""
	else:
		interval_c = interval(num_tr)
	url = 'http://saraksti.rigassatiksme.lv/wap/index.php?a=p.routes_directions&transport_id='
	url += tr_id
	url += '&interval='
	url += str(interval_c)
	url += '&day='
	url += str(num_week)
	url += '&t=wml&l=en'
	try:
		page = urllib2.urlopen(url)
	except:
		print "No Internet connection =("
	else:
		try:
			pagestr = page.read()
			tempstring = "<b>"+str(num_tr)+"</b>"
			pagestr = re.split(tempstring, pagestr)
			pagestr = pagestr[1]
			pagestr = re.split("</p>", pagestr)
			pagestr = pagestr[0]
			pagestr = re.split("<br/>", pagestr)
			pagestr = pagestr[:2]
			for a in pagestr:
				a = a.strip()
				a.decode('utf-8')
			result = []
			for a in pagestr:
				m = re.search(r'<a href="(.+)">(.+)</a>', a)
				result += [[m.group(1), m.group(2)]]
		except:
			print "Error parsing page"
			return 0
		else:
			return result
	#We've got tuple with bus stop list URLs for selected bus - [[url1, a-b], [url2, b-a]]
