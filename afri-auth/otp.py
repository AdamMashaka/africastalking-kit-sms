from .security import generate_otp
from .storage import redis_client
from .providers.africastalking import send_sms
from .config import OTP_EXPIRY


class OTPAuth:

    async def send_otp(self, phone: str):

        code = generate_otp()

        redis_client.setex(
            f"otp:{phone}",
            OTP_EXPIRY,
            code
        )

        message = f"Your OTP code is {code}"

        await send_sms(phone, message)

        return {
            "success": True,
            "message": "OTP sent successfully"
        }

    async def verify_otp(self, phone: str, code: str):

        stored_code = redis_client.get(f"otp:{phone}")

        if not stored_code:
            return {
                "success": False,
                "message": "OTP expired"
            }

        if stored_code != code:
            return {
                "success": False,
                "message": "Invalid OTP"
            }

        redis_client.delete(f"otp:{phone}")

        return {
            "success": True,
            "message": "OTP verified successfully"
        }