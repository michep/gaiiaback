from fastapi import FastAPI
import openai
import uvicorn

openai.api_key = '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'

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

uvicorn.run(app=app,port=8080)
