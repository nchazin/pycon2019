import asyncio
from unittest import TestCase

import cat
from loop_runner import LoopRunner


class Tests(TestCase):

    def setUp(self):
        self.runner = LoopRunner(asyncio.new_event_loop())
        self.runner.start()

    def tearDown(self):
        self.runner.stop()
        self.runner.join()

    def test_forward(self):
        garfield = cat.Cat('Garfield')
        result = self.runner.run_coroutine(herd(garfield, 'forward'))
        self.assertTrue(result)


async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


