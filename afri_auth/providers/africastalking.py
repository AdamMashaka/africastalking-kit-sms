from afri_auth.config import AFRICASTALKING_USERNAME
import africastalking

# from afri_auth.config import (
#     AFRICASTALKING_USERNAME,
#     AFRICASTALKING_API_KEY
)

def get_sms_client():

    africastalking.initialize(
        AFRICASTALKING_USERNAME,
        AFRICASTALKING_API_KEY
    )

    return africastalking.SMS
sms = africastalking.SMS


async def send_sms(phone, message):

    sms = get_sms_client()

    response = sms.send(
        message,
        [phone]
    )

    return response