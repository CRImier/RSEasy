## -*- coding: utf-8 -*-
import urllib2
import re
def parsedb(url, num_tr):
  try:
		page = urllib2.urlopen(url)
		pagestr = page.read()
	except:
		print "Internet connection trouble, no page received from server or something else. Check your Internet connection."
	else:
		# Now let's parse, mazafaka! Using re.split, mazafaka!
		# TODO - rewrite using regex
		try:
			tempstring = "<b>"+str(num_tr)+"</b>"
			pagestr = re.split(tempstring, pagestr)
			pagestr = pagestr[1]
			pagestr = re.split("</card>", pagestr)
			pagestr = pagestr[0]
			pagestr = re.split("<br/>", pagestr, 2)
			pagestr = pagestr[2]
			pagestr = re.split("<br/>", pagestr)
			for i in pagestr:
				i = re.split("</p>", i)
				#They see me splittin'
				#They hatin'
			tempi = len(pagestr) - 1
			pagestr = pagestr[:tempi]
			dirarr = []
			for i in pagestr:
				i = i.strip()
				i = re.split("<b>", i)
				i = i[1]
				i = re.split("</b>", i)
				i[0] = i[0].strip()
				#But then somebody appends some words in brackets in i[1]. SOOKAA.
				i[1] = re.split(r'([0-9 ]*)[(](.+)[)]([0-9 ]*)', i[1]) #A wild REGEX appears
				if len(i[1])>1:
					i[1] = i[1][1:]
					i[1] = i[1][:(len(i[1])-1)]
					i[1] = [i[1][0] + i[1][2]]
				i[1] = i[1][0]
				temparr = i[1].split()
				i[0] = i[0][:(len(i[0]) - 1)]
				for m in temparr:
					dirarr += [[i[0] , m]]
			#So we've got full array in the form we need it. 
			return dirarr
		except:
			print "Page received from server is broken or no longer has the same structure."
			return 0
