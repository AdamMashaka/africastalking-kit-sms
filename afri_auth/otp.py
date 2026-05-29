from .security import generate_otp
from .storage import redis_client
from .providers.africastalking import send_sms
from .config import OTP_EXPIRY


class OTPAuth:

    def __init__(
        self,
        username=None,
        api_key=None,
        expiry=None
    ):

        self.username = username
        self.api_key = api_key
        self.expiry = expiry or OTP_EXPIRY

    @classmethod
    def from_env(cls):
        return cls()

    async def send_otp(self, phone: str):

        code = generate_otp()

        redis_client.setex(
            f"otp:{phone}",
            self.expiry,
            code
        )

        message = f"Your OTP code is {code}"

        await send_sms(
            phone=phone,
            message=message,
            username=self.username,
            api_key=self.api_key
        )

        return {
            "success": True,
            "message": "OTP sent successfully",
            "expires_in": self.expiry
        }

    async def verify_otp(
        self,
        phone: str,
        code: str
    ):

        stored_code = redis_client.get(
            f"otp:{phone}"
        )

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

        redis_client.delete(
            f"otp:{phone}"
        )

        return {
            "success": True,
            "message": "OTP verified successfully"
        }