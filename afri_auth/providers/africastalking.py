import africastalking
from afri_auth.config import (
    AFRICASTALKING_USERNAME,
    AFRICASTALKING_API_KEY
)

africastalking.initialize(
    AFRICASTALKING_USERNAME,
    AFRICASTALKING_API_KEY
)

sms = africastalking.SMS


async def send_sms(phone: str, message: str):
    response = sms.send(message, [phone])
    return response