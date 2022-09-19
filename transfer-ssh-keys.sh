#!/bin/bash
for server in `cat server-GETS.txt`;
do
    sshpass -p "PASSWORD" ssh-copy-id -i ~/.ssh/id_rsa.pub user@$server
done
~
