#!/usr/bin/python3
from scapy.all import *

a = IP()
a.dst = '10.0.2.4'
b = ICMP()
p = a/b
send(p)