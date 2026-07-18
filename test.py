import os 
from dotenv import load_dotenv 
load_dotenv()

os.environ("OPENAI_API_KEY") = os.getenv("OPENAI_API_KEY")
openai.chat.completions.create(
    model= "gpt-4o-mini"
    messages=[role: user, content: "what is agentic ai?"]
)

openai.chat.conpletions.create(
    model= "gpt-4o-mini",
    message =["role":"user", "content": "what is llm engineering?"]
)

openai.chat.completions.create(
    model = "gpt-4o-mini",
    message = [{"role":"user", "coontent": "what is llm engineering ?"}]
)

os.environ("OPENAI_API_KEY") = os.getenv("OPENAI_API_KEY")
client = OpenAI()

openai.chat.completions.completions.create(
    model = "gpt-4o-mini",
    message=[{"role": "user", "content": "what is agentic engineering?"}]
)

openai.chat.completions.create()






openai.chat.completions.create(
    model = "gpt-5 nano", content = [{"role":"user", "message":"what is llm engineering?"}]
)




response = openai.chat.completions.create(
    model= "gpt-5-nano", message=[{"role":"user", "content":"what is llm engineering?"}]
)
 
request = response.choices(0).message.content 
print ("request")




















import os 
from dotenv import load_dotenv
load_dotenv()

response  = openai.chat.completions.create()
