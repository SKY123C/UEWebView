import threading
import asyncio
import uvicorn
from .app import main


class FastAPIServerThread(threading.Thread):
    def __init__(self, host: str = "127.0.0.1", port: int = 8050):
        super().__init__()
        self.host = host
        self.port = port
        self.daemon = True

    def run(self):
        asyncio.run(self.start_server())
    
    async def start_server(self):
        config = uvicorn.Config(main.app, host=self.host, port=self.port, reload=True)
        server = uvicorn.Server(config)
        server.force_exit
        await server.serve()

server_thread = FastAPIServerThread()
server_thread.daemon = True


class ServerManager:

    def start_server(self):
        if not server_thread.is_alive():
            server_thread.start()


manager = ServerManager()


