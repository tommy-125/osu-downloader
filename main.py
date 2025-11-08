import uvicorn
import asyncio
from src.api.auth import osuAuth
from src.web.server import app

serverConfig = uvicorn.Config(app, host="127.0.0.1", port=8000)
server = uvicorn.Server(serverConfig)
asyncio.run(osuAuth.getAuthorization(server))
def main():
    osuAuth.getCredential()
    osuAuth.getAuthorization(server)
main()
