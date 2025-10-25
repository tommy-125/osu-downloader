import time
import requests
import webbrowser
import os
from src.core import config

from dotenv import set_key

class OsuAuth:
    def authorize(self):
        access_token = config.get_access_token()
        if access_token:
            token_time = float(config.get_access_token_time())
            expires_in = float(config.get_expires_in())
            now = float(time.time())
            isExpired = True if now-token_time >= expires_in else False
            if isExpired:
                self.refreshToken()
        else:
            self.getCode()

    def getCode(self):
        url = "https://osu.ppy.sh/oauth/authorize"
        params = {
            "client_id" : config.get_client_id(),
            "redirect_uri" : "http://localhost:8000",
            "response_type" : "code"
        }
        response = requests.get(url, params=params)
        webbrowser.open(response.url)


    def getTokenFromCode(self,code):
        url = "https://osu.ppy.sh/oauth/token"
        headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        data = {
            "client_id" : str(config.get_client_id()),
            "client_secret" : config.get_client_secret(),
            "code" : str(code),
            "grant_type" : "authorization_code",
            "redirect_uri" : "http://localhost:8000"
        }
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # HTTP 錯誤會丟出例外
            tokenData = response.json()
            now = time.time()
            set_key(config.env_path, "ACCESS_TOKEN", tokenData["access_token"])
            set_key(config.env_path, "REFRESH_TOKEN", tokenData["refresh_token"])
            set_key(config.env_path, "ACCESS_TOKEN_TIME", str(now))
            # 立即更新 process environment，讓其他程式碼可以即時讀到新 token
            os.environ["ACCESS_TOKEN"] = tokenData["access_token"]
            os.environ["REFRESH_TOKEN"] = tokenData["refresh_token"]
            os.environ["ACCESS_TOKEN_TIME"] = str(now)
            print(tokenData)
        except requests.exceptions.RequestException as e:
            print("HTTP 請求發生錯誤:", e)

    def refreshToken(self):
        url = "https://osu.ppy.sh/oauth/token"
        headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        data = {
            "client_id" : config.get_client_id(),
            "client_secret" : config.get_client_secret(),
            "grant_type" : "refresh_token",
            "refresh_token" : config.get_refresh_token()
        }
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # HTTP 錯誤會丟出例外
            tokenData = response.json()
            now = time.time()
            set_key(config.env_path, "ACCESS_TOKEN", tokenData["access_token"])
            set_key(config.env_path, "REFRESH_TOKEN", tokenData["refresh_token"])
            set_key(config.env_path, "ACCESS_TOKEN_TIME", str(now))
            # 立即更新 process environment，讓其他程式碼可以即時讀到新 token
            os.environ["ACCESS_TOKEN"] = tokenData["access_token"]
            os.environ["REFRESH_TOKEN"] = tokenData["refresh_token"]
            os.environ["ACCESS_TOKEN_TIME"] = str(now)
            
        except requests.exceptions.RequestException as e:
            print("HTTP 請求發生錯誤:", e)

# 創建全域實例
osuAuth = OsuAuth()