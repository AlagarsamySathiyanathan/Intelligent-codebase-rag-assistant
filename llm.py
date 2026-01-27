from groq import Groq
import os
from dotenv import load_dotenv # Keeps API keys out of source code

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY")) # reads our Groq API key, here it used for all requests

def query_groq(context,question):  # Accepts retrieved code chunks(context) and user question
    prompt=f"""
you are a senior software engineer.
Answer the question using ONLY the context below.


Context:
{context}

Question:
{question}

"""
    
    response=client.chat.completions.create(      # calls Groq's API
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2 # reduce halucisiation ,more factual,better code explanations
    )

    return response.choices[0].message.content # Acess LLm response and return only the answer text