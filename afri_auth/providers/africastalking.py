import africastalking

from afri_auth.config import (
    AFRICASTALKING_USERNAME,
    AFRICASTALKING_API_KEY
)


def get_sms_client():

    if not AFRICASTALKING_USERNAME:
        raise ValueError(
            "AFRICASTALKING_USERNAME is missing"
        )

    if not AFRICASTALKING_API_KEY:
        raise ValueError(
            "AFRICASTALKING_API_KEY is missing"
        )

    africastalking.initialize(
        AFRICASTALKING_USERNAME,
        AFRICASTALKING_API_KEY
    )

    return africastalking.SMS


async def send_sms(phone, message):

    sms = get_sms_client()

    return sms.send(
        message,
        [phone]
    )
