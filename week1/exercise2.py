#!/usr/bin/env python3
# Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets.
# Print out the octets in decimal, binary, and hex.
#
# Your program output should look like the following:
#
# $ python exercise2.py
# Please enter an IP address: 80.98.100.240
#
#    Octet1         Octet2         Octet3         Octet4
#------------------------------------------------------------
#      80             98             100            240
#   0b1010000      0b1100010      0b1100100     0b11110000
#     0x50           0x62           0x64           0xf0
#------------------------------------------------------------
#
#Four columns, fifteen characters wide, a header column, data centered in the column.

from __future__ import print_function

try:
    ip_addr = raw_input("Please enter an IP address: ")
except NameError:
    ip_addr = input("Please enter an IP address: ")

#split IP address between periods
octet = ip_addr.split(".")

print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(octet[0], octet[1], octet[2], octet[3]))
print(
    "{:^15}{:^15}{:^15}{:^15}".format(
        bin(int(octet[0])),
        bin(int(octet[1])),
        bin(int(octet[2])),
        bin(int(octet[3]))
        )
    )
print(
    "{:^15}{:^15}{:^15}{:^15}".format(
        hex(int(octet[0])),
        hex(int(octet[1])),
        hex(int(octet[2])),
        hex(int(octet[3]))
        )
    )
print("-" * 60)
