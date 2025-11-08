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
        "q" : "key=4 artist=\"camellia\""
    }
    response = requests.get(url, headers=headers, params=params)

    data = response.json()  # Python dict
    beatmapIDForDownload = []
    while True:
        beatmapsetCount = len(data["beatmapsets"])

        for i in range(beatmapsetCount): # 遍歷每個beatmapset
            beatmapCount = len(data["beatmapsets"][i]["beatmaps"])
            beatmapList = data["beatmapsets"][i]["beatmaps"]
            for j in range(beatmapCount): # 遍歷每個beatmap
                if(beatmapList[j]["mode"] == "mania"):
                    beatmapIDForDownload.append(beatmapList[j]["id"])

        if data["cursor_string"] is None:
            break
        else:
            params["cursor_string"] = data["cursor_string"]
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
    print(beatmapIDForDownload)
    return beatmapIDForDownload