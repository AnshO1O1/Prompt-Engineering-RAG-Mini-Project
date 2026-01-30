import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = "llama-3.1-8b-instant"

def answer_question(context, question, prompt):
    if not context or not context.strip():
        return (
            "Answer:\nInformation not available.\n\n"
            "Evidence:\nNone\n\n"
            "Confidence:\nLow"
        )

    full_prompt = f"""
You are a policy assistant.

Rules:
- Use ONLY the provided context
- Do NOT use outside knowledge
- If the answer is not in the context, say so clearly

Context:
{context}

Question:
{question}

Answer in this format:
Answer:
Evidence:
Confidence:
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.0,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()