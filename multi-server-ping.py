import os
import subprocess
import sys
myserver=sys.argv[1]
with open(myserver, "r") as file:
    servers=file.read().split()

    for ip in servers:
        #print(ip)
        reply = subprocess.run(['ping', '-c', '3', '-n',ip],stdout=subprocess.PIPE)

        if reply.returncode == 0:
            print(ip,'is Alive')
        else:
            print(ip,'ia Unreachable')
