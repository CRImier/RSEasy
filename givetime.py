# coding=utf-8
def givetimes(schedarr, times):
	import datetime
	now_time = datetime.datetime.now() #Get time
	x = 0 #Counter variable
	hn = now_time.hour
	mn = now_time.minute
	commin = (hn * 60) + mn #Minutes from start of day by now
	try: #Try to ensure you don't fall out of array boundaries
		while int(schedarr[x][0])<hn :
			x += 1
		while(int(schedarr[x][0]) * 60) + int(schedarr[x][1]) <= commin : 
				x += 1
	except:
		print "--:--"
	else:
		try:
			while times>=0:
				print str(schedarr[x][0])+":"+str(schedarr[x][1])
				x += 1
				times -= 1
		except:
			print "--:--"
	
