#!/usr/bin/env python3
from scapy.all import *

example = rdpcap('pcaps/arp.pcap')
for packet in example:
    packet.show()
