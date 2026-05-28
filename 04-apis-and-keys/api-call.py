from openai import OpenAI
from dotenv import load_dotenv, dotenv_values

load_dotenv()

config=dotenv_values(".env")
hf_token=config.get("HF_TOKEN")

client = OpenAI(
  base_url="https://router.huggingface.co/v1",
  api_key=hf_token
)

completion  = client.chat.completions.create(
  model="moonshotai/Kimi-K2-Instruct-0905",
  max_tokens=256,
  messages=[{ "role": "user", "content": "How many G in huggingface?" }]
)

print(completion.choices[0].message)