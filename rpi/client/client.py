import base64
import socket
import sys
from time import sleep

from Crypto.Cipher import AES
from Crypto import Random



class Client:
    def __init__(self, ip_addr, port_num, aes_key):
        self.key = bytes(str(aes_key), encoding = "utf8")
        # Connect to TCP socket at ip_addt:port_num
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip_addr, port_num))


    def encrypt(self, message):
        # Make message length multiple of block size
        raw = self._pad(message)
        iv = Random.new().read(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))


    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)


    def send(self, action, power_details=None):
        # Fill dummy values if power_details not provided
        p = power_details if power_details else {'voltage': 0, 'current': 0, 'power': 0, 'cumpower': 0}
        # Format message per server expectations
        message = '#{}|{}|{}|{}|{}'.format(action, p['voltage'], p['current'], p['power'], p['cumpower'])
        self.sock.send(self.encrypt(message))


    def end(self):
        self.send('logout')
        self.sock.close()



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Invalid number of arguments')
        print('python client.py [IP address] [Port] [AES key]')
        sys.exit()

    ip_addr = sys.argv[1]
    port_num = int(sys.argv[2])
    key = sys.argv[3]

    if not(len(key) == 16 or len(key) == 24 or len(key) == 32):
        print("AES key must be either 16, 24, or 32 bytes long")
        sys.exit()

    client = Client(ip_addr, port_num, key)
    input('Press enter to send action')
    client.send('test', {'voltage': 0, 'current': 1, 'power': 2, 'cumpower': 3})
    sleep(2)
    client.end()
