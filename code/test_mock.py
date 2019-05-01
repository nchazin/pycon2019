import asyncio
from unittest import TestCase
from unittest.mock import Mock, patch

import cat

async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


class Tests(TestCase):

    @patch('cat.Cat.move')
    def test_forward(self, move_mock):
        garfield = cat.Cat('Garfield')
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(herd(garfield, 'forward'))
        move_mock.assert_called_with('forward')



