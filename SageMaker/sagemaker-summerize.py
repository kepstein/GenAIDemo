#!/usr/bin/env python

from sagemaker.huggingface import HuggingFacePredictor
	
predictor = HuggingFacePredictor('hf-bart-large-cnn-summarization')

intro_text = """
You are a research assistant. You job is to succinctly summarize text. Make sure you capture all the most important points in the text. Summarize the following text:
For all the pixels spilled about the promises of generative AI, it’s starting to feel like we’re telling the same 
story over and over again. AI is serviceable at document summarization and shows promise in customer service 
applications. But it generates fictions (the industry prefers the euphemistic and anthropomorphizing term 
“hallucinates”) and is limited by the data on which it’s trained. Now that we’re at what seems like a plateau in the AI 
hype wave, where do startups and their investors see opportunities to use AI to help businesses operate in meaningful ways? 
Venture capitalists we spoke with said efficiencies in internal workflows—whether coding, office-wide data search, or 
meeting and document summarization—were the biggest driving forces behind enterprise adoption right now. “If you take a 
look at the macro, we’re kind of coming from a period of very rapid sort of Covid-driven growth for most businesses that 
then turned into a bit of a headwind once the pandemic was over,” Ilya Fushman, a partner at Kleiner Perkins, said. 
“Those [headwinds] have driven a really strong need for efficiency.” 
"""

prediction = predictor.predict({
	"inputs": intro_text
})

print("Summarized text:\n" + prediction[0]['summary_text'])
