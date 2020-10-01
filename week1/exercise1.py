#!/usr/bin/env python3

# Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses).
# Print these three variables to standard output using a single print statement.
#
# Make your print statement compatible with both Python2 and Python3.
#
# If you are using either Linux or MacOS make your program executable by adding a shebang line and by changing the files permissions (i.e. chmod 755 exercise1.py).

# make compatible with python2
from __future__ import print_function

ip_addr1 = "8.8.8.8"
ip_addr2 = "208.67.222.222"
ip_addr3 = "1.1.1.1"

print("Common public DNS servers are " + ip_addr1 + ", " + ip_addr2 + ", and " + ip_addr3)
