
    
"""whena a call is made to the llm the text are first chunked, depending on the ytpe 
of data that is fed into the llm, then the chunksare then converted into tokens
"""
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
tokens = encoding.encode("my name is godsfavour")
print(tokens)


for token_id in tokens:
    token_text = encoding.decode([token_id])
    print (f"{token_id} = {token_text}")
    
