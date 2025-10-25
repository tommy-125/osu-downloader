import uvicorn
import asyncio
from src.api.auth import osuAuth
from src.web.server import app
from src.core.config import config
from src.api import beatmap

serverConfig = uvicorn.Config(app, host="127.0.0.1", port=8000)
server = uvicorn.Server(serverConfig)

def main():
    asyncio.run(osuAuth.authorize(server))
main()