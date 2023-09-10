import os
import socket
import json
import rpc_function


current_path = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_path, "..", "setting", "config.json")
with open(config_path, "r") as file:
    config = json.load(file)


def main() -> None:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    buf_size = config["buffer_size"]
    server_address = config["server_address_file_path"]
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print(f"Starting up on {server_address}")

    sock.bind(server_address)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            print(f"connection from {client_address}")
            while True:
                data = connection.recv(buf_size)
                data_str = data.decode("utf8")
                print("Received " + data_str)
                if data:
                    # print("json.loads(data_str)")
                    # print(json.loads(data_str))
                    response_json_dict = rpc_function.executeRpcFunction(
                        json.loads(data_str)
                    )
                    # print("response_json_dict")
                    # print(response_json_dict)
                    response_json_str = json.dumps(response_json_dict)
                    # print("response_json_str")
                    # print(response_json_str)
                    connection.sendall(response_json_str.encode())
                    # connection.sendall("sample response".encode())
                else:
                    print("no data from", client_address)
                    break
        except Exception as e:
            print(e)
            connection.sendall("Error".encode())
        finally:
            print("Closing current connection")
            connection.close()
            return None


if __name__ == "__main__":
    main()
