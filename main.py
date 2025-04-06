from fastapi import FastAPI
from controllers.AccountController import router as bank_router

app = FastAPI()

app.include_router(bank_router)

@app.get("/")
def read_root():
    return {"message": "Hello, Bank App!"}
