#!/usr/bin/env python

import openai
import os

# Use this to set up an ENV variable with a ref to the 1Password credential.
# I have automated this by adding the below line in the .env file in this directory and setting up autoenv. 

# export OPENAI_API_KEY="op://Personal/OpenAI - Test Key/api key"     

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

intro_text = """
For all the pixels spilled about the promises of generative AI, it’s starting to feel like we’re telling the same 
story over and over again. AI is serviceable at document summarization and shows promise in customer service 
applications. But it generates fictions (the industry prefers the euphemistic and anthropomorphizing term 
“hallucinates”) and is limited by the data on which it’s trained.

Now that we’re at what seems like a plateau in the AI hype wave, where do startups and their investors see 
opportunities to use AI to help businesses operate in meaningful ways?
Venture capitalists we spoke with said efficiencies in internal workflows—whether coding, office-wide data search, 
or meeting and document summarization—were the biggest driving forces behind enterprise adoption right now.
“If you take a look at the macro, we’re kind of coming from a period of very rapid sort of Covid-driven growth 
for most businesses…that then turned into a bit of a headwind once the pandemic was over,” Ilya Fushman, a 
partner at Kleiner Perkins, said. “Those [headwinds] have driven a really strong need for efficiency.”
"""

messages=[{"role": "system", "content": "You are a research assistant. You job is to succintly summarize text. Make sure you capture all the most important points in the text"},
          {"role": "user", "content": "summarize this article for me please: " + intro_text + ""}]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=500,
    temperature=0.8,
    messages = messages
)

# print(response)
print("\n"+response.choices[0].message.content)


