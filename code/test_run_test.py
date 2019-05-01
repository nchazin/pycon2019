import asyncio
from unittest import TestCase


async def async_calculator(a, b):
    while(1):
        x = a + b



class Tests(TestCase):

    def test_1_1(self):
        loop = asyncio.get_event_loop()
        val = loop.run_until_complete(async_calculator(1,1))
        self.assertEqual(1, val)

    def test_1_0(self):
        loop = asyncio.get_event_loop()
        val = loop.run_until_complete(async_calculator(1,0))
        self.assertEqual(0, val)

    def test_1_1(self):
        loop = asyncio.get_event_loop()
        val = loop.run_until_complete(async_calculator(1,1))
        self.assertEqual(1, val)
