import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI



# openai=OpenAI()


# messages= [
#     {"role":"system", "content": "youre a professional software engineer"},
#     {"role":"user", "content":"what is software engineering?"}
# ]

# response = openai.chat.completions.create(
#     model = "gpt 4o-mini", messages= "messages"
# )

# output = response.choices[0].message.content
# print (output)



###runnning open source models with olama 

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
api_key = os.getenv("OLLAMA_API_KEY")

message = [
    {"role":"system", "content":"youre a rofessional software engineer"},
    {"role": "user", "content":"what is sotware engneering? explain in maximum detail"}
]

response = ollama.chat.completions.create(
    model ="llama3.2:3b", messages = message
)

output= response.choices[0].message.content
print(output) 