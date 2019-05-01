import asyncio
from unittest import TestCase
from unittest.mock import MagicMock, patch

import cat


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Tests(TestCase):

    @patch('cat.Cat.move', new_callable=AsyncMock)
    def test_forward(self, move_mock):
        garfield = cat.Cat('Garfield')
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(herd(garfield, 'forward'))
        move_mock.assert_called_with('forward')



async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)
