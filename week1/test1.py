# Python2 import that will support Python3 print() function
from __future__ import print_function

#ip_addr = "8.8.8.8"
try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")

print(ip_addr)
