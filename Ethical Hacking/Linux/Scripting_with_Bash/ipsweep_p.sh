#!/bin/bash  tell the system that this is a bash file. 

ping 192.168.182.132 
# - keeps pinging IP
ping 192.168.182.132 -c 1
# - pings ip once 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ping 192.168.182.132 -c 1 > ip.txt

cat ip.txt 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#extract data from the ping 

#grep looks for a specific term or phrase 

cat ip.txt | grep "64 bytes"
    #returns 192.168.182.132:

cat ip.txt | grep "64 bytes" | cut -d ' ' -f 4 | tr -d ":"
    #  - "-d" - delimiter , "-f" fields
    #  - tr -d ":" - gets rid of : after ip 
    #returns 192.168.182.132

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
 #create new bashfile - 
    mousepad ipsweep.sh 

    if ["$1" == ""]
    then 
    echo "You must specify IP ADDY"
    echo "Syntax: ./ipsweep.sh 192.168.182"
    
    else
    for ip in `seq 1 254` ; do 
    ping -c 1 $1.$ip | grep "64 bytes" | cut -d ' ' -f 4 | tr -d ":" &
    done
    fi
     
     # $1 is the argument after the 0 argument which in this case is call the for loop "./ipsweep"
     # loops thorugh 1-254 for the last field in the ip untill it hits 254. Point of this is to get active ips in the subnet.
     # & - lets multipule instances of the loop to run at once.

     # after you can store result in a file with 

     ./ipsweep.sh 192.168.4 > ips.txt #stores ips 