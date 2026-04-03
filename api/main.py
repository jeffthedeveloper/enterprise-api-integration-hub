from fastapi import FastAPI

app = FastAPI()

@app.get(""/"")
def read_root():
    return {""message"": ""Bem-vindo à API FastAPI""}

@app.post(""/create/"")
def create_item(item: str):
    return {""item"": item}
