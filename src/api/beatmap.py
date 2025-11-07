import json
import requests
from src.core import config

def searchBeatmap():
    url = "https://osu.ppy.sh/api/v2/beatmapsets/search"
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {config.get_access_token()}"
    }
    params = {
        "m" : "3",
        "q" : "key=4"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()  # Python dict
    # 寫入 JSON 檔案
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("已將結果寫入 beatmaps.json")