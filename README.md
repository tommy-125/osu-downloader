# osu-downloader

A small Python script for authenticating with the osu! API and preparing to manage beatmap downloads.

## Overview
This project was originally intended to download ".osz" beatmap files directly using the osu! API.  
However, due to recent API restrictions, direct download access via API is no longer supported.  
The script now only implements **Authorization Code Grant** and **Client Credentials Grant**,  
laying the foundation for future osu!-related automation tools.


## Example Usage

### Authorization Code Grant
```
import uvicorn
import asyncio
from src.api.auth import osuAuth
from src.web.server import app

serverConfig = uvicorn.Config(app, host="127.0.0.1", port=8000)
server = uvicorn.Server(serverConfig)
asyncio.run(osuAuth.getAuthorization(server))
```

### Client Credentials Grant
```
from src.api.auth import osuAuth

osuAuth.getCredential()
```
