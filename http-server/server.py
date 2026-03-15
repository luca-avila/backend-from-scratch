import socket

from utils import parse_http_request, build_http_response

HOST = "0.0.0.0"

PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    method, path, version, headers = parse_http_request(data)
                    print(f"Received {method} request for {path}")
                    response = build_http_response(200, f"Hello! You requested {path}")
                except Exception as e:
                    print(f"Error parsing request: {e}")
                    response = build_http_response(400, "Bad Request")
                conn.sendall(response)
