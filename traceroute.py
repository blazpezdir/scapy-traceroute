#!/usr/bin/python3
from scapy.all import *
import time

host = "google.com";
MAX_HOPS = 100

# Build IP layer
a = IP()
a.dst = host

# Build ICMP layer
b = ICMP()

print("Target: %s" % a.dst)

# For each hop across routers (TTL decreseas by 1 each time routing happens)
for ttl in range(1, MAX_HOPS):
    # Set TTL
    a.ttl = ttl
    # Stack layers together
    p = a / b

    # Send packet and listen for response
    response = sr1(p, verbose=0, timeout=2)
    if response is None:
        # No reply =(
        print("%d hops away: " % ttl, "No reply =(")
    elif response.type == 0:
        # We've reached our destination
        print("%d hops away: " % ttl, "DONE")
        break
    else:
        # We're in the middle somewhere
        print("%d hops away: " % ttl, response.src)
else:
  print("Loop ended without reaching destination! Increase the max TTL value to reach your destination.")

