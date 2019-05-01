import asyncio
from unittest import TestCase

import herd_router
from loop_runner import LoopRunner


class Tests(TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        self.herd_router = herd_router.HerdRouter(self.loop)
        self.runner = LoopRunner(self.loop)
        self.runner.start()

    def tearDown(self):
        self.runner.stop()
        self.runner.join()

    def test_command(self):
        self.herd_router.add_command('test')
        assert 'test' in self.herd_router.commands



