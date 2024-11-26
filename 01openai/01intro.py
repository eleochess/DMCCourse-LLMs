import openai

client = openai.OpenAI(
    api_key="COPIA TU API KEY AQUI",
)

prompt = "cuál es la capital de Francia"
chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'system', 'content': 'Eres un asistente virtual'},
        {'role': 'user', 'content': prompt}
    ],
    model="gpt-4o",
)

res = chat_completion.to_dict()

print(res['choices'][0]['message']['content'].strip())