

import sys
from scapy.all import *

# Listens and filter covert traffic, denoted with an "E" flag
def parse(pkt):
	flag=pkt['TCP'].flags
	if flag == 0x40:
		char = chr(pkt['TCP'].sport)
	        sys.stdout.write(char)

# Main
sniff(filter="tcp", prn=parse)
