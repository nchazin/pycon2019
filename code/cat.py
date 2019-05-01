import asyncio
import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.mood = DISPLEASED

    async def move(self, direction):
        if self.mood == PLEASED:
            await asyncio.sleep(random.uniform(0, 5))
            self.mood = DISPLEASED
            return True
        return False

    def pet(self):
        self.mood = PLEASED


DISPLEASED = False
PLEASED = True

