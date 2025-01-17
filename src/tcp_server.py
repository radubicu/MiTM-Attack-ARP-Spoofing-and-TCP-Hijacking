# TCP Server
import socket
import logging
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 10000
addr = '198.7.0.2'
server_address = (addr, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portnul portul %d", addr, port)
sock.listen(5)

try:
    while True:
        logging.info('Asteptam conexiui...')
        conn, address = sock.accept()
        logging.info("Handshake cu %s", address)
        try:
            for i in range(3):
                data = conn.recv(1024)
                
                if not data:
                    raise Exception()
                
                logging.info('Content primit: "%s"', data)
                message = b'Am primit: ' + data
                conn.send(message)
                logging.info("Mesaj trimis: %s", message)
        except Exception as e:
            print(e)
        finally:
            print("Conexiune inchisa...")
            conn.close()
finally:
    sock.close()
