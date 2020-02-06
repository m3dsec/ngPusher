#!/usr/bin/python3

import os
import sys
import time
from shutil import which

def usage():
	print("https://github.com/m3dsec/ngPusher")
	print("python3 ngpusher.py [options]")
	print("   -F --forward   start ngrok with tcp port 22; upload generated subdomains")
	print("                  to your private git repo for later use")
	print("   -K --kill      kill ngrok process ")

if len(sys.argv) != 2:
	#print(len(sys.argv))
	usage()
	exit()

arg = sys.argv[1]

def checkSSHService():
	try:
		sshStatus = os.system('systemctl is-active --quiet ssh')
		#print(status)  # will return 0 for active else inactive.
		if sshStatus == 0:
			print("[*] SSH SERICE ALREADY STARTED..")
		else:
			print("[*] STARTING SSH SERVICE..")
			os.system("service ssh start")
	except:
		print("[!] SSH DEAMON NOT FOUND, TRY \"sudo apt install openssh-server\"")
		exit()

def checkNgrok():
	ngStatus = which("ngrok") is not None
	print('[*] CHECKING FOR NGROK EXISTENCE')
	time.sleep(1)
	if ngStatus is True:
		print('   . ngrok well configured. ')
		pass
	elif ngStatus is False:
		print('[!] NGROK IS MISSING')
		print('   . ngrok is not installed on your system, visit "https://ngrok.com/" for more info')
		print('   . please consider adding your ex file to your path ex:/usr/bin/ngrok')

def killOldProcess():
	time.sleep(1)
	print("[*] KILLING OLD NGROK PROCESS...")
	os.system("kill $(ps aux |grep -i ngrok |awk '{print $2}'|tr '\n' ' ') & ")
	time.sleep(1)

def ngroking():
	print("[*] FROWARDING WITH NGROK TCP SERVER...")
	os.system('ngrok tcp 22 --log stdout --log-format term |tee info.txt &')
	time.sleep(2)  # wait for the file to get created
	print("[*] EXTRACTING THE HOST AND PORT...")
	os.system("cat info.txt |grep url|rev |awk '{print $1}' |rev |cut -d':' -f2 |cut -c3- > host.txt &") 	# GET HOST DOMAIN 
	time.sleep(0.3)
	os.system("cat info.txt |grep url|rev |awk '{print $1}' |rev |cut -d':' -f3 > port.txt &") 	# GET PORT LOGIN INFO
	time.sleep(0.3)
	hostFile = open('host.txt', 'r') 	# SAVE INTO FILES
	portFile = open('port.txt', 'r')
	pushFile = open('push.txt', 'w')
	time.sleep(0.3)
	print('[*] WRITE FILES FOR YOUR GIT FILE') 	# WRITE TO PUSH FILE
	os.system("cat host.txt port.txt > push.txt")
	for h in hostFile: 	# GET DATA FROM FILES into VARS
		host = h.strip("\n")
	for p in portFile:
		p = p.strip("\n")
		port = p
	time.sleep(0.3) 	# PRINT RESULTS
	print('[*] SSH TUNNEL INTO : ' + str(host) + " " + str(port))
	portFile.close()
	hostFile.close()
	pushFile.close()


def gitPush():
	# PUSH TO GITHUB OR anonfileupload
	# at this part you'll need to store your creds befor using the script
	# at it may ask you for your github creds with 
	# $ git config --global credential.helper store
	# $ git pull
	print("[*] ADD FILES TO UPLOAD...")
	#os.system("git add push.txt")
	#os.system("git add info.txt")
	os.system("git add port.txt")
	os.system("git add host.txt")
	os.system("git commit -m 'python3 update' -q ")
	os.system("git remote add origin https://github.com/[USERNAME ]/[YOUR REPO].git") # modify on this one
	os.system("git remote")
	print("[*] PUSH TO GITHUB")
	os.system("git push origin master -q")
	print("[*] CHECK YOUR FILE: ")
	#print("   . https://github.com/[USERNAME]/[YOUR REPO]/blob/master/push.txt")
	#print("   . https://github.com/USERNAME]/[YOUR REPO]/blob/master/host.txt")
	#print("   . https://github.com/USERNAME]/[YOUR REPO]/blob/master/port.txt")


if arg.lower() == "--forward" or arg.lower() == "-f":
	checkSSHService()
	checkNgrok()
	killOldProcess()
	ngroking()
	gitPush()

if arg.lower() == "--kill" or arg.lower() == "-k":
	print("[*] KILLING NGROK SERVICE...")
	time.sleep(1)
	os.system("kill $(ps aux|grep ngrok|grep -v \"grep\"|awk '{print $2}'|tr '\n' ' ')")

