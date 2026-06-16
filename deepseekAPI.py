import requests
api_key="不告诉你喵"
response=requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "你好"}]
    }
)
print(response.json()["choices"][0]["message"]["content"])
