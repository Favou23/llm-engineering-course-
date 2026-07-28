day 1
 run models locally with ollama
* write code to call openai frontier models
*distinguish between the system prompt and user prompt
*summarization( a function that scrapes the data of a web by inputing a urla as a parameter and then uses llm to summarize the content of the web)

day2
* know the building blocks to get to llm mastery
* be set up for success
* recognize the leading frontier models and how to use them

3 different dimensions of llm engineering
models                       tools                 techniques
open-source                  huggingface           Apis
closed-source                langchain             multi- shot prompting
multi-modal                  gradio                rag
architecture                 weight and biases     fine-tuning
selecting                    modal                 Agentization

day 3
**** what im doing today****
compae the top frontier models: chatgpt vs reasoning
appreciate what they do well
recognize where they struggle


***llms come in 3 flavours which are ****

*base models--- predict the sequence of orders of the next probability of word
*chat/instruct model --- trained to work in the prompt style that describe the whole chat in one peice of information in the and user prompt manner..
reasoning/thinking models--- they are trained to force output their thinking steps and give their answers 
*** frontier models and their chat products***
openai--- models:gpt----chat: chtgpt
Antropic--- models: claude--- chat:claude
google--- models: gemmini---chat:gemini advance
x.ai--- models:grok---chat:grok
deepseek--models:deepseek---chat:deepseek

*** mind blowing performance from frontier llms***
synthensizing information, answering a question in depth with a structured, well researched anwer and often including a summary
flashing out skeleton from a couple of notes, building out a well crafted, or blog post and iterating on it with you until perfect 
coding-- the abilith to write and debug code is remarkable, for overtaken stackoverflow  as the resource for engineers 


*** limitations of frontier models***
specialized domains most are not phd leve, but closing in
recent events, limited knowledge beyond training cut off, date: code often uses legacy apis/models
can confidently make mistakes some curious blindspos, canjump too conclusions when coding 

*** day 4***
understanding transformers
--tokens
tokenization with tiktoken
context window and api cost 
