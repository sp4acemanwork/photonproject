import socket
import random
import time
import unittest


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







