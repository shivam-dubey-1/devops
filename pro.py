import time
import socket
import faktory

with faktory.connection() as client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("fak", 0))
    while True:
        client.queue("add", args=(1, 2), queue="default")
        time.sleep(1)

        client.queue("subtract", args=(10, 5), queue="default")
        time.sleep(1)

        client.queue("multiply", args=(8, 8), queue="default")
        time.sleep(1)