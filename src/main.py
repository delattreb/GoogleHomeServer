"""
main.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 09/01/2018
"""

import socket
import json
from lib import com_config, com_logger


def Main():
    # Config
    conf = com_config.Config()
    #conf.setconfig()
    config = conf.getconfig()
    # Logger
    logger = com_logger.Logger()
    logger.debug(str(config['APPLICATION']['name']) + " " + str(config['APPLICATION']['version']))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    #address = (ip, int(config['server']['port']))
    # For Linux
    address = ('', int(config['server']['port']))
    logger.debug("[*] Server START: " + str(ip) + " : " + str(config['server']['port']))
    server.bind(address)

    while True:
        server.listen()
        (connexion, addr) = server.accept()
        logger.debug("[*] Connection from: " + str(addr[0]) + " : " + str(addr[1]))

        data = connexion.recv(1024).decode()
        if (str(data) == "disconnect"):
            connexion.send("Bye".encode())
            logger.info("[*] Disconnect")
            connexion.close()
            server.close()
            break
        elif not data:
            pass
        elif (len(data) > 0):
            logger.debug("[*] Receive data from the client: " + str(data))
            logger.debug("Processing data")
            logger.info(decodeJson(data))
        else:
            logger.warning("Invalid command")
            connexion.send("Invalid command".encode())

def decodeJson(data):
    obj = json.loads(data)
    return obj['user']['profile']['display_name']

if __name__ == '__main__':
    Main()
