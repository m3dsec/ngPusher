# ngPusher
Expose your host using ssh, github and ngrok 

the main idea is to expose your local machine without buying a VPS or buying a ngrok service.
<br>
every time you run the script, ngrok start in the background & send the generated host and port to your
github (public) repo, in the other machine or phone or whatever, you launch the sshlogin.py script with your username, and you get a connection

Tested in a Debian 5 machine, android os with temux terminal
<br>
python3 (requests,re and json module)
<br>
<br>
requrement :
- github repo
- ngrok already configuered --> https://ngrok.com/
- ssh client
mhm, 
also you need to modify on scripts to get started
