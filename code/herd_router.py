import asyncio
import threading

class HerdRouter(threading.Thread):

    def __init__(self, loop):
        self._loop = loop
        self._rlock = threading.RLock()
        self.commands = set()

    # thread safe
    async def _add_command(self, key):
        with self._rlock:
            self.commands.add(key)
        return True

    # actual work is done in a thread safe manner
    def add_command(self, key):
        result = asyncio.run_coroutine_threadsafe(self._add_command(key), self._loop)
        result.result()



