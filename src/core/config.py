from pathlib import Path
from dotenv import load_dotenv, set_key
import os

class Config:
    def __init__(self):
        self.env_path = Path(".") / ".env"
        load_dotenv(dotenv_path=self.env_path)
    
    def get_access_token(self):
        return os.getenv("ACCESS_TOKEN")
    
    def get_refresh_token(self):
        return os.getenv("REFRESH_TOKEN")
    
    def set_access_token(self, token):
        set_key(self.env_path, "ACCESS_TOKEN", token)

    def set_refresh_token(self, token):
        set_key(self.env_path, "REFRESH_TOKEN", token)
    
    def get_client_id(self):
        return os.getenv("CLIENT_ID")
    
    def get_client_secret(self):
        return os.getenv("CLIENT_SECRET")
    
    def get_access_token_time(self):
        return os.getenv("ACCESS_TOKEN_TIME")

    def get_expires_in(self):
        return os.getenv("EXPIRES_IN")
# 創建一個全局實例
config = Config()