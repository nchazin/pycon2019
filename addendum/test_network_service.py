import asyncio
import socket
from unittest import TestCase


from loop_runner import LoopRunner
import network_service
import uvloop


TESTPORT = 8888

import uvloop

class TestUVLoop(TestCase):

    def setUp(self):
        self.loop = uvloop.new_event_loop()
        self.runner = LoopRunner(self.loop)
        self.runner.start()

    def tearDown(self):
        self.runner.stop()
        self.runner.join()

    def test_simple_request(self):
        server = network_service.RequestServer(self.loop, TESTPORT)
        self.runner.run_coroutine(server.start_server())

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', TESTPORT)
        sock.connect(server_address)
        sock.send("reframe-experimently".encode())

        data = sock.recv(32)
        self.assertEqual(data.decode(),'Ack reframe-experimently\n')

        sock.close()
