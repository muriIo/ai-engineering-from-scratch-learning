from dotenv import load_dotenv, dotenv_values
import json
from urllib.request import Request, urlopen

load_dotenv()

config=dotenv_values(".env")
hf_token=config.get("HF_TOKEN")

url="https://router.huggingface.co/v1/chat/completions"
headers={
  "Content-Type": "application/json",
  "Authorization": "Bearer " + hf_token
}

body = json.dumps({
  "messages": [
          {
              "role": "user",
              "content": "How many G in huggingface?"
          }
      ],
  "model": "moonshotai/Kimi-K2-Instruct-0905:cheapest",
  "stream": False
}).encode()

req = Request(url, data=body, headers=headers, method="POST")

with urlopen(req) as response:
    body = response.read().decode("utf-8")
    result = json.loads(body)

print(result)