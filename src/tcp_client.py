# TCP client
import socket
import logging
import time
import sys
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)


port = 10000
adresa = '198.7.0.2'
server_address = (adresa, port)

def generate_string():
    length = random.randint(5, 10)
    r_string = ""
    for i in range (length):
        r_string += chr(random.randint(64, 123))

    return r_string


while True:
    time.sleep(1)
    try:
        print(f"Trying {server_address}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        # sock.settimeout(5.0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.connect(server_address)
            logging.info('Handshake cu %s', str(server_address))
        except:
            sock.close()
            continue
        for i in range(3):
            time.sleep(2)
            mesaj = generate_string()
            logging.info("Mesaj trimis %s", mesaj)
            try:
                sock.send(mesaj.encode('utf-8'))
                data = sock.recv(1024)
                
                if not data:
                    raise Exception()
                
                logging.info('Content primit: "%s"', data)
                time.sleep(2)
            except:
                print("Conexiune terminata!")
                break
        sock.close()
        
    except KeyboardInterrupt:
        sys.exit(0)

logging.info('closing socket')
sock.close()
