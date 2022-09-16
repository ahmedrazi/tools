import os
import subprocess

#with open('myserver.txt').read().splitlines()
with open("myserver.txt", "r") as file:
    servers=file.read().split()

    for ip in servers:
        #print(ip)
        reply = subprocess.run(['ping', '-c', '3', '-n',ip],stdout=subprocess.PIPE)
    
        if reply.returncode == 0:
            print(ip,'is Alive')
        else:
            print(ip,'ia Unreachable')
