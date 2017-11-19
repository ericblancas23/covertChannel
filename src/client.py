

import sys
from scapy.all import *

pkt = None

# Prase command line argument
def usage():
	if len(sys.argv) != 2:
		print "Usage:", sys.argv[0], "<host_ip>"
		sys.exit()

# Craft the packet to send
def craft(character):
	global pkt
	global dest
	dest = str(sys.argv[1])
	char = ord(character) # covert character to decimal value
	pkt=IP(dst=dest)/TCP(sport=char, dport=RandNum(0, 65535), flags="E")
	return pkt

# Send the message based on the user input
def client():
	while True:
		message = raw_input('Enter your message: ')
		message += "\n"
		print "Sending data: " + message
		for char in message:
			new_pkt = craft(char)
			send(new_pkt)

# Main
usage()
client()
