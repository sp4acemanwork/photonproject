import sys
import os
import socket
import random
import time
import unittest
from server import handler
from server import usr
from server import udp_handler


class testprogram(unittest.TestCase):
    def setUp(self):
        self.bufferSize = 1024
        self.serverAddressPort = ("127.0.0.1", 7500)
        self.clientAddressPort = ("127.0.0.1", 7501)
        self.UDPServerSocketReceive = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocketReceive.bind(self.serverAddressPort)

    def check_start_game(self) -> bool:
        print("")
        print("waiting for start game signal")
        received_data = ' '
        while received_data != '202':
            received_data, address = self.UDPServerSocketReceive.recvfrom(self.bufferSize)
            received_data = received_data.decode('utf-8')
            self.assertEquals(received_data, '202')
        return True
# send hit user then expect hit user hardware id to be returned

    def check_player_hit_player(self, player1: str, player2: str):
        try:
            message = str(player1) + ":" + str(player2)
            self.UDPServerSocketTransmit.sendto(str.encode(str(message), self.clientAddressPort))
            hituser, address = self.UDPServerSocketReceive.recvfrom(self.bufferSize)
            hituser.decode('utf-8')
            self.assertEquals(hituser, player2)
        except socket.timeout:
            self.fail

    def player_scored(self, player: str, base: str):
        try:
            message = str(player) + ":" + str(str)
            self.UDPServerSocketTransmit.sendto(str.encode(str(message), self.clientAddressPort))
            score, address = self.UDPServerSocketReceive.recvfrom(self.bufferSize)
            score = score.decode('utf-8')
            score = int(score)
            self.assertIsInstance(score, int)
        except socket.timeout:
            self.fail

    def check_end_game(self) -> bool:
        print("")
        print("waiting for start game signal")
        received_data = ' '
        check = received_data != '221'
        received_data, address = self.UDPServerSocketReceive.recvfrom(self.bufferSize)
        received_data = received_data.decode('utf-8')
        if check:
            return False
        else:
            return True

    def tearDown(self):
        self.UDPServerSocketReceive.close()
        self.UDPServerSocketTransmit.close()


print("running test")


print("ports will be ")
bufferSize = 1024
serverADP = ("127.0.0.1", 7500)
clientADP = ("127.0.0.1", 7501)

print(f"bufferSize {bufferSize}")
print(f"serverADP {serverADP}")
print(f"clientADP {clientADP}")

users_with_teams = [
    ("Alice", 1, 101, "RED"),
    ("Bob", 2, 102, "GREEN"),
    ("Charlie", 3, 103, "RED"),
    ("Diana", 4, 104, "GREEN"),
    ("Eve", 5, 105, "RED"),
    ("Frank", 6, 106, "GREEN"),
]

print("instant server")

server = handler(clientADP[0], serverADP[1], clientADP[1], bufferSize)

print(f"adding users {users_with_teams}")

for name, id, eq_id, team in users_with_teams:
    print(f"adding {name}")
    server.add_player(name, id, eq_id, team)
