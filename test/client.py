import os
import socket
import sys
import json

current_path = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_path, "..", "setting", "config.json")
with open(config_path, "r") as file:
    config = json.load(file)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

buf_size = config["buffer_size"]
server_address = config["server_address_file_path"]
print(f"connecting to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

messages = [
    b'{"method": "floor", "params": [42.7], "param_types": ["float"], "id": 1}',
    b'{"method": "nroot", "params": [2, 64], "param_types": ["int", "int"], "id": 1}',
    b'{"method": "reverse", "params": ["abcdef"], "param_types": ["str"], "id": 1}',
    b'{"method": "validAnagram", "params": ["abc", "cba"], "param_types": ["str", "str"], "id": 1}',
    b'{"method": "sort", "params": [["b", "a", "c"]], "param_types": ["list[str]"], "id": 1}',
]

try:
    for msg in messages:
        print(f"sending -> {msg}")
        sock.sendall(msg)
        sock.settimeout(2)
        try:
            while True:
                data = str(sock.recv(buf_size))
                if data:
                    print("Server response: " + data)
                else:
                    break
        except TimeoutError:
            print("Socket timeout, ending listening for server messages")

finally:
    print("closing socket")
    sock.close()
    exit()
