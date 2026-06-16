import requests
api_key="sk-292f9a67b33f4b7e9af32d34b3a3625d"
response=requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "你好"}]
    }
)
print(response.json()["choices"][0]["message"]["content"])
