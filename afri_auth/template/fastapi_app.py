from fastapi import FastAPI
from afri_auth.fastapi import OTPRouter

app = FastAPI()

app.include_router(
    OTPRouter,
    prefix="/auth",
    tags=["Authentication"]
)


@app.get("/")
def home():
    return {
        "message": "Afri Auth Running"
    }