import asyncio


class RequestServer:
    def __init__(self, loop, port):
        self.loop = loop
        self.port = port

    async def handle_request(self, reader, writer):
        request = await reader.read(100)
        data = request.decode().strip()
        writer.write(f"Ack {data}\n".encode())
        await writer.drain()
        writer.close()

    async def start_server(self):
        coro = asyncio.start_server(self.handle_request,
                                    '127.0.0.1',
                                    self.port,
                                    loop=self.loop)
        server = await coro


def main():
    loop = asyncio.get_event_loop()
    server = RequestServer(loop, 8888)
    loop.create_task(server.start_server())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

