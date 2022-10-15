from scapy.all import * 

def packet_parser(packet) :
    print(packet.summary())


if __name__ == "__main__": 
    sniff(iface="enxfe183c584ec9", prn= packet_parser, store= 0) 