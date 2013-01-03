## -*- coding: utf-8 -*-
import urllib2
import re

def getstops(url, num_tr):
  try:
		page = urllib2.urlopen(url)
		pagestr = page.read()
	except:
		print "Internet connection trouble, no page received from server or something else. Check your Internet connection."
	else:
		try:
			tempstring = "<b>"+str(num_tr)+"</b>"
			pagestr = re.split(tempstring, pagestr)
			pagestr = pagestr[1]
			pagestr = re.split("<p>", pagestr)
			pagestr = pagestr[1]
			pagestr = re.split("</p>", pagestr)
			pagestr = pagestr[0]
			pagestr = re.split("<br/>", pagestr)
			for i in pagestr:
				i = i.strip()
				#They see me strippin'
				#They hatin'
			pagestr = pagestr[:(len(pagestr) - 1)]
			result = []
			for i in pagestr:
				m = re.search(r'<a href="(.+)">(.+)</a>', i)
				result += [[m.group(1), m.group(2)]]
			return result
		except:
			print "Page received from server is broken or no longer has the same structure."
			return 0


