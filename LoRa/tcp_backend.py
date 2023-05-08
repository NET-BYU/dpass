import socket
# import random
import os
import sys
import signal
import time

class TCP:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    def server(self, port, ip_address):
        def handler(sig, frame):
            print('You pressed Ctrl+C!')
            self.socket.close()
            sys.exit(0)
        signal.signal(signal.SIGINT, handler)
        counter = 0
        print(port, ip_address)
        self.socket.bind((ip_address, port))
        self.socket.listen()
        conn, addr = self.socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:",counter)
                counter += 1
                # conn.sendall(data)
    def client(self, port, ip_address, rate,packet_size):
        def handler(sig, frame):
            print('You pressed Ctrl+C!')
            self.socket.close()
            sys.exit(0)
        signal.signal(signal.SIGINT, handler)
        print(port,ip_address,rate)
        self.socket.connect((ip_address, port))
        print("connected")
        sleep_time = 1 - rate
        counter = 0
        while True:
            check = self.socket.sendall(os.urandom(packet_size))
            print("packet:",counter,check)
            counter += 1
            time.sleep(sleep_time)

        pass