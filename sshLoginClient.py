#!/usr/bin/python3
# get the port from repo file
# python3 sshlogin.py username - specify only the username <----
# if no host specified use the default one

# making my repo public is not secure as i may put my ssh login into exposure
# just temporary solution
import sys
import os
import requests

if len(sys.argv) != 2:
	print('python3 sshlogin.py username - specify the username')
	exit()

# GET THE USERNAME FROM THE USER
userName = sys.argv[1]
port = ''
host = ''
# GET HOST AND PORT FROM THE PUBLIC REPO
pushR = requests.get("https://raw.githubusercontent.com/[USERNAME]/[REPO NAME]/master/push.txt")
portR = requests.get("https://raw.githubusercontent.com/[USERNAME]/[REPO NAME]/master/port.txt")
hostR = requests.get("https://raw.githubusercontent.com/[USERNAME]/[REPO NAME]/master/host.txt")

for chr in portR.text:
	port += chr.strip("\n")

print("YOUR PORT IS : " + port)	
for chr in hostR.text:
	host += chr.strip("\n")

print("YOUR host IS : " + host)

# SSH IN
# print("ssh %s@%s -p %s" %(userName, host, port))
os.system("ssh %s@%s -p %s" %(userName, host, port))


