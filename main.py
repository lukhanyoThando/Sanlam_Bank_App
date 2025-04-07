from fastapi import FastAPI, APIRouter
from controllers.AccountController import router as bank_router

app = FastAPI()

app.include_router(bank_router)

@bank_router.get("/bank")
def get_accounts():
    return {"message": "return a list of bank accounts."}

# Include the router into the FastAPI app
app.include_router(bank_router)

@app.get("/")
def read_root():
    return {"message": "Hello, Bank App!"}
