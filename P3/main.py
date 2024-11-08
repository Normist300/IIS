from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return({"message", "Здарова"})

@app.get("/hello/{name}")
def read_name(name: str):
    return {"message": f"привет {name}!"}