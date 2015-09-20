#!/usr/bin/python
import sys, getopt, os
import urllib2
from xml.dom import minidom
from os.path import expanduser

url= "http://server.lolbrothers.com/server/status2.php?host=fre.lolbrothers.com&port=27045"

user = expanduser("~")
filepath = user+"/data.xml"

doc = None

def DownloadXML():
	req = urllib2.Request(url)
	res = urllib2.urlopen(req)
	fo = open(filepath, "w+")
	fo.write(res.read())
	fo.close()
	doc = minidom.parse(filepath)


def getElementsbyName(element):
	name = doc.getElementsByTagName(element)[0]
	return name.firstChild.data 
	
def getPlayers():
	name = doc.getElementsByTagName("players")[0]
	return name.firstChild.data 

def getMaxPlayers():
	name = doc.getElementsByTagName("maxplayers")[0]
	return name.firstChild.data 

def getMap():
	name = doc.getElementsByTagName("mapname")[0]
	return name.firstChild.data 

def getServerName():
	name = doc.getElementsByTagName("servername")[0]
	return name.firstChild.data 

def getAppID():
	name = doc.getElementsByTagName("appid")[0]
	return name.firstChild.data

def getGameVersion():
	name = doc.getElementsByTagName("gameversion")[0]
	return name.firstChild.data

def getServerPort():
	name = doc.getElementsByTagName("serverport")[0]
	return name.firstChild.data

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"he:pamlsivtd",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'error  - LeonServer.py -e <input element> -p <out player> -a <out max player> -l <out map> -s <out servername> -i <out appid> -v <out version> -t <out port> -d <downloadxml>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'LeonServer.py -e <input element> -p <out player> -a <out max player> -l <out map> -s <out servername> -i <out appid> -v <out version> -t <out port> -d <downloadxml>'
			sys.exit()
		elif opt in ("-e", "--ifile"):
			print getElementsbyName(arg)
			#print arg
		elif opt in ("-p"):
			print getPlayers()
		elif opt in ("-a"):
			print getMaxPlayers()
		elif opt in ("-l"):
			print getMap()
		elif opt in ("-s"):
			print getServerName()
		elif opt in ("-i"):
			print getAppID()
		elif opt in ("-v"):
			print getGameVersion()
		elif opt in ("-t"):
			print getServerPort()
		elif opt in ("-d"):
			DownloadXML()

if __name__ == "__main__":
	if os.path.isfile(filepath) is False:
		DownloadXML()
	else:
		try:
			doc = minidom.parse(filepath)
		except:
			DownloadXML()	
	main(sys.argv[1:])

#
#print "servertags: " + getElementsbyName("servertags")
#print "players: "+  getPlayers() + " / " + getMaxPlayers()
#print "Map: " + getMap()
#print "Server name: " + getServerName()
#print "Version: " + getGameVersion() + ", appid:" + getAppID()
#print "port: " + getServerPort()
