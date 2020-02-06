# ngPusher
expose your host using ssh, github and ngrok
-----

the idea is to expose your local machine without 
buying a VPS or even buying ngrok service every 
time you run the script, ngrok start in the back-
ground & send the generated host and port to your
github (public) repo, in the other machine or 
phone or whatever, you launch the sshlogin.py 
script with your username, and you get loged in

Tested in a Debian 5 machine, android os with 
temux terminal, 
python3 (requests,re and json module)

you may need to modify on files to get started
 . create a repo in github & init the repo in the script working dir
 . modify on files as needed
 . launch ngPusherGITClient.py in your client machine
 . launch sshlogin.py from an other host to get connected
happy sshing
