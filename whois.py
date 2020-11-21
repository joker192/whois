import socket
import os
import time
os.system("pkg install figlet -y")
os.system("clear")
os.system("figlet whois")
print("==================================")
print("         made by bad_boy        ")
print(" my telegram id: @Bad_boy_468     ")
print("==================================")
print("[1]domin = org , com , net")
print("[2]domin = ir , uk or.... ")
print("========================================")
print("[!]Usage --> target.com or target.tk or....")
print("========================================")
hacker=int(input("Enter : "))
if hacker == 1:
    site = input("Enter URL Site : ").lower()
    print("Loading.....")
    time.sleep(1)
    server1 = "whois.internic.net"
    joker = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    joker.connect((server1,43))
    joker.send((site + "\r\n").encode())
    king = joker.recv(10000)
    print(king.decode())
elif hacker == 2:
    site2 = input("Enter URL Site : ").lower()
    print("Loading....")
    time.sleep(1)
    server2 = "whois.iana.org"
    kinger = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    kinger.connect((server2,43))
    kinger.send((site2 + "\r\n").encode())
    op = kinger.recv(10000)
    print(op.decode())
