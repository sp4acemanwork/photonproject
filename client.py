import socket

class udp_client:
    def __init__(self, server_ip: str, server_port: int, buffer_size: int):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"UDP client created for server {self.server_ip}:{self.server_port}")

    def send_data(self, data: bytes):
        self.sock.sendto(data, (self.server_ip, self.server_port))
        print(f"Sent message: {data} to {self.server_ip}:{self.server_port}")

    def receive_data(self):
        data, addr = self.sock.recvfrom(self.buffer_size)
        print(f"Received message: {data} from {addr}")
        return data, addr

def __main__():
    print("starting client")
    udp_client1 = udp_client("127.0.0.1", 7501, 1024)
    udp_client1.send_data(b"Add Player")
    data, addr = udp_client1.receive_data()
    print(f"Equipment codes from Server: {data}")

__main__()
