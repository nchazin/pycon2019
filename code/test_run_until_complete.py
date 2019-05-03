import asyncio
from unittest import TestCase

import cat

async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


class Tests(TestCase):

    def test_forward(self):
        garfield = cat.Cat('Garfield')
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(herd(garfield, 'forward'))
        loop.close()
        self.assertTrue(result)




