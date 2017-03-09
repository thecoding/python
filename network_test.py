#!/user/bin/env python
# coding=UTF-8
# import socket

# socket.setdefaulttimeout(2)

# s = socket.socket()
# s.connect(("124.42.240.131",21))
# ans = s.recv(1024)

# print ans

import optparse
import socket
def connScan(tgtHost,tgtPort):
	try:
		connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		print('[+]%d/tcp open' % tgtPort)
		connSkt.close()
	except Exception, e:
		print('[-]%d/tcp closed' % tgtPort)

def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = socket.gethostbyname(tgtHost)
	except Exception, e:
		print("[-]Cannot resolve '%s':Unknown host" % tgtHost)
		return
	try:
		tgtName = socket.gethostbyaddr(tgtIP)
		print('\n[+] Scan Results for:'+tgtName[0])
	except Exception, e:
		print('\n[+] Scan Results for:'+tgtIP)
	socket.setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print('Scanning port '+ str(tgtPort))
		connScan(tgtHost,int(tgtPort))

portScan('www.wo56.com',[80,443,3389,1433,23])
