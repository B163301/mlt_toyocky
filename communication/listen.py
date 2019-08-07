# -*- coding: utf-8 -*-
#import subprocess
import socket
import string
import os
import random
import time
import re

import speak
 
host = "localhost"
port = 10500
 

time.sleep(5)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

pattern = r'WHYPO WORD=\"(.+)\" CLASSID=\"([0-9]+)\"'
repattern = re.compile(pattern)

CLASSID_COMMAND = '0'
 

print()
print("TOYOCKY")
print()


try:
    data = ""
     
    while True:
        while (1):
            if '</RECOGOUT>\n.' in data:
                #print(data)
                #print()
                strTemp = ""
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    if index != -1:
                        rslt = repattern.findall(line)
                        word, classid = rslt[0]
                        if classid == CLASSID_COMMAND:
                            speak.jtalk(word)
                        strTemp += "{}:{}\n".format(word, classid)
                print(strTemp)
                data = ""
            else:
                data += str(sock.recv(1024).decode('utf-8'))
 

except KeyboardInterrupt:
    print("\n\n===!!ATTENTION!!===")
    print("FOR TO KILL JULIUS PROCESS")
    print("CHECK the process id of JULIUS by `ps` command")
    print("KILL JULIUS PROCESS by `kill xxxx` command. xxxx is number of JULIUS PROCESS")
    print("===!!ATTENTION!!===\n\n")
