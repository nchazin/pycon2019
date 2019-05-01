import pytest

import cat

async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


class Tests:

    @pytest.mark.asyncio
    async def test_forward(self):
        garfield = cat.Cat('Garfield')
        result = await herd(garfield, 'forward')
        assert result


