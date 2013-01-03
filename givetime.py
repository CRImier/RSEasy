import datetime
import time
def check_transtp(transtp):
  if transtp == "tram" or transtp == "bus" or transtp == "trolleybus"  or transtp == "night_bus":
		return True
	else:
		return False
weekday = raw_input("Enter number of day of week: (press Enter for today's day) ")
if weekday == '':
	now_date = datetime.date.today()
	weekday = now_date.isoweekday()
elif int(weekday) <= 7:
	weekday = int(weekday)
#Choose tram or trolleybus or bus or night_bus #To remake: and (transtp != "tram" or transtp != "bus" or transtp != "trolleybus"  or transtp != "night_bus")
transtp = ''
while check_transtp(transtp) == False:
	transtp = raw_input("Enter type of transport - tram, bus, night_bus or trolleybus: ") #Check input!
transid = ''
while transid == '' or transid.isdigit() == False:
	transid = raw_input("Enter number of transport: ")
transid = int(transid)
#	->Correct info about transport type, number and day of week (if not default) (to getdir.py)
#	<-Information about directions (from getdir.py)
import getdir
buses = getdir.getdirs(transtp, transid, weekday)
if buses == 0:
	raise Exception("Error while getting bus list!")
counter = 0
for bus in buses: #Printing out stop list for choosing
	bus += [counter]
	print str(counter)+"	-	"+bus[1]
	counter += 1
choice = ''
while choice == '' or int(choice) < 0 or int(choice) >= counter:
	choice = raw_input("Enter direction number: ") 
choice = int(choice)
#	->Needed direction (to getstop.py)
#	<-Bus stops (from getstop.py)
import getstop
url = "http://saraksti.rigassatiksme.lv/wap/index.php"+str(buses[choice][0])
#Fucking problem. We get "&amp;" instead of "&"
#Replace ALL the "&amp;"!
import re
temparray = re.split("amp;", url)
url = ''
for a in temparray:
	url += a
#Yeah, that's good.

stops = getstop.getstops(url, transid)
if stops == 0:
	raise Exception("Error while getting stop list!")
counter = 0
for stop in stops:
	stop += [counter]
	print str(counter)+"	-	"+stop[1]
	counter += 1
choice = ''
while choice == '' or int(choice) < 0 or int(choice) >= counter:
	choice = raw_input("Enter stop number: ") 
choice = int(choice)
url = "http://saraksti.rigassatiksme.lv/wap/index.php"+str(stops[choice][0])
temparray = re.split("amp;", url)
url = ''
for a in temparray:
	url += a
#	->Needed bus stop (to parsedb.py)
#	<-Nearest buses scheduled (from parsedb.py)
import parsedb
array = parsedb.parsedb(url, transid)
if array == 0:
	raise Exception("Error while getting timetable!")

#	->Bus timeline (to givetime.py)
#	<-Nearest buses scheduled (from givetime.py)
import givetime
givetime.givetimes(array, 5)
#That's all, folks.
