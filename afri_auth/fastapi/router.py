from fastapi import APIRouter
from pydantic import BaseModel
from afri_auth.otp import OTPAuth

router = APIRouter()

otp_auth = OTPAuth()


class SendOTPRequest(BaseModel):
    phone: str


class VerifyOTPRequest(BaseModel):
    phone: str
    code: str


@router.post("/send-otp")
async def send_otp(data: SendOTPRequest):
    return await otp_auth.send_otp(data.phone)


@router.post("/verify-otp")
async def verify_otp(data: VerifyOTPRequest):
    return await otp_auth.verify_otp(
        data.phone,
        data.code
    )