import uvicorn
import asyncio
from src.api.auth import osuAuth
from src.web.server import app
from src.core.config import config
serverConfig = uvicorn.Config(app, host="127.0.0.1", port=8000)
server = uvicorn.Server(serverConfig)

async def main():
    # 啟動伺服器（非阻塞）
    server_task = asyncio.create_task(server.serve())

    # 這裡可以做授權流程
    osuAuth.authorize()
    while not config.get_access_token():
        await asyncio.sleep(0.5)  # 每 0.5 秒檢查一次
    # 等待伺服器完全關閉
    server.should_exit = True
    await server_task
    
asyncio.run(main())