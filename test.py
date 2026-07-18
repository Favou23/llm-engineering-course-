import os 
from dotenv import load_dotenv 
load_dotenv()
from openai import OpenAI

client = OpenAI()


messages = [
    {"role": "system", "content": "youre a professional software engineeri"},
    {"role":"user", "content": "what is software engineering?"}
]

response =  client.chat.completions.create(
    model = "gpt-5-nano", messages = messages
),

response.choice[0].message.content

























import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

openai=OpenAI()


messages= [
    {"role":"system", "content": "youre a professional software engineer"},
    {"role":"user", "content":"what is software engineering?"}
]

response = openai.chat.completions.create(
    model = "gpt 4o-mini", messages= "messages"
)

output = response.choices[0].message.content
print (output)