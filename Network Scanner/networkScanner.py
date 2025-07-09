import socket
from datetime import datetime

net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("enter the starting number: "))
en1 = int(input("Enter the last number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
    ports_to_check = [21, 22, 23, 80, 139, 445]
    for port in ports_to_check:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((addr, port))
        s.close()
        if result == 0:
            return True
    return False

def run1():
    for ip in range(st1, en1):
        add = net2 + str(ip)
        if scan(add):
            print(add, " is live")

run1()
t2 = datetime.now()
total = t2 - t1
print("Scanning completed in ", total)