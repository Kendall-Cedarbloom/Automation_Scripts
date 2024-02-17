from scapy.all import *

L2 = Ether(src="0C:66:35:0B:00:00", dst="0C:D8:25:05:00:00")

send = sendp(L2)

L2.show

