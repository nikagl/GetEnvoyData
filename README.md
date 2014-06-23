GetEnvoyData
============

This Python scripts allows retrieval of the Envoy Local API from Enphase:
http://enphase.com/global/files/Envoy-API-Technical-Brief.pdf

Please note, you need Envoy software release R3.9 or later to be able to read your local Envoy status.

Try not to read your Envoy more than once every 5 minutes as the PV Inverters will only produce data every 5 minutes.

Install Python 2.7:
https://www.python.org/download/releases/2.7

Tested with Python 2.7.6 but 2.7.7 should work too.

Run the script using the command line:
c:\Python27\python.exe Envoy.py

After successfull retrieval you can do anything with the data, like put it in a database, push it to PVOutput, etc.:
	write_logging("*** Doing something here with wattsNow: %s" % wattsNow)
