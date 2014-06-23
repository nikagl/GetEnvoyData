#! /usr/bin/python

import sys
import time
import urllib
import json
from datetime import datetime

# Command line:
#
# C:\Python27\python.exe Envoy.py
#

def write_logging(loggingtext):
	logf.write("%s\n" % loggingtext)
	print loggingtext
	
def read_envoy():
	retries = 0
	success = False
	wattHoursToday = 0
	wattHoursSevenDays = 0
	wattHoursLifetime = 0
	wattsNow = 0
	while (success == False and retries < 10):
		try:
			write_logging("Opening URL to get Envoy status")
			url = "http://192.168.111.35/api/v1/production"
			write_logging("URL: %s" % url)
			request = urllib.urlopen(url).read()
			dict = json.loads(request)
			wattHoursToday = dict.get('wattHoursToday')
			wattHoursSevenDays = dict.get('wattHoursSevenDays')
			wattHoursLifetime = dict.get('wattHoursLifetime')
			wattsNow = dict.get('wattsNow')
			write_logging("Retrieved wattHoursToday : %s" % wattHoursToday)
			write_logging("Retrieved wattHoursSevenDays : %s" % wattHoursSevenDays)
			write_logging("Retrieved wattHoursLifetime : %s" % wattHoursLifetime)
			write_logging("Retrieved wattsNow : %s" % wattsNow)
			success = True
		except:
			retries += 1
			write_logging("Retrying: %d (max 10), delay 20 seconds." % retries)
			write_logging("Exception type: %s" % sys.exc_info()[0])
			write_logging("Exception value: %s" % sys.exc_info()[1])
			write_logging("Exception traceback: %s" % sys.exc_info()[2])
			time.sleep(20)
	return success, wattHoursToday, wattHoursSevenDays, wattHoursLifetime, wattsNow

#logf = open('envoy.log', 'a')	# use a for unlimited logfile
logf = open('envoy.log', 'w')	# use w for new logfile at runtime
write_logging("")
tstamp = datetime.now()
write_logging("-- envoy.py start: %s" % tstamp)
success, wattHoursToday, wattHoursSevenDays, wattHoursLifetime, wattsNow = read_envoy()

if (not success):
	write_logging("Could not get envoy status. Please try again later...")
else:
	write_logging("*** Doing something here with wattsNow: %s" % wattsNow)

write_logging("-- envoy.py done: %s" % tstamp)
logf.close()
