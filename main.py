from fastapi import FastAPI

app=FastAPI()

@app.post("/naga")

def greetings():
    return ("welcome erripuka")


# uvicorn main:app --reload --host "0.0.0.0" --port 8080
#