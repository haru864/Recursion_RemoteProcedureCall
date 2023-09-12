import os
import socket
import json
import multiprocessing
import rpc_function

buf_size = None
request_id_to_socket = {}


def handle_client(connection, client_address):
    global buf_size, request_id_to_socket
    try:
        print(f"connection from {client_address}")
        while True:
            data = connection.recv(buf_size)
            data_str = data.decode("utf8")
            print("Received " + data_str)
            if data:
                data_dict = json.loads(data_str)
                request_id = data_dict["id"]
                request_id_to_socket[request_id] = connection
                print(f"request pool -> {request_id_to_socket}")
                response_json_dict = rpc_function.executeRpcFunction(
                    data_dict["method"], data_dict["params"], data_dict["param_types"]
                )
                response_json_str = json.dumps(response_json_dict)
                print(f"Sending {response_json_str}")
                connection.sendall(response_json_str.encode())
                request_id_to_socket.pop(request_id)
            else:
                print(f"no data from {client_address}")
                break
    except Exception as e:
        print(e)
        connection.sendall("Error".encode())
    finally:
        print("Closing current connection")
        connection.close()


def main() -> None:
    current_path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(current_path, "..", "setting", "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = config["server_address_file_path"]
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print(f"Starting up on {server_address}")

    sock.bind(server_address)
    sock.listen(1)

    global buf_size, request_id_to_socket
    buf_size = config["buffer_size"]
    request_id_to_socket = {}

    with multiprocessing.Pool(processes=4) as pool:
        while True:
            connection, client_address = sock.accept()
            pool.apply_async(handle_client, [connection, client_address])


if __name__ == "__main__":
    main()
