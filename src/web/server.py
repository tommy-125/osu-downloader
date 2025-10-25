from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from src.api import osuAuth

app = FastAPI()

@app.get("/")
async def root(request: Request):
    osuAuth.code = request.query_params.get("code")
    return HTMLResponse(f"""
       <h2>授權成功!</h2> 
    """)
