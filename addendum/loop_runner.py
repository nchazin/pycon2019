import asyncio
import threading

class LoopRunner(threading.Thread):

    def __init__(self, loop):
        threading.Thread.__init__(self, name='runner')
        self.loop = loop

    def run(self):
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_forever()
        finally:
            if self.loop.is_running():
                self.loop.close()

    def run_coroutine(self, coroutine):
        result = asyncio.run_coroutine_threadsafe(coroutine, self.loop)
        return result.result()

    def _stop(self):
        self.loop.stop()

    def run_in_thread(self, callback, *args):
        return self.loop.call_soon_threadsafe(callback, *args)

    def stop(self):
        return self.run_in_thread(self._stop)


