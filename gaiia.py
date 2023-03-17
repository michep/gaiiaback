from fastapi import FastAPI
import openai
import uvicorn
from apikey import API_KEY

openai.api_key = API_KEY

app: FastAPI = FastAPI()

@app.post("/chat")
async def chat(messages: list[dict]):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        max_tokens=2048,
        temperature=0,
    )
    message = completion.choices[0].message
    return {'message': message.content}

uvicorn.run(app=app, host='0.0.0.0', port=8185)
