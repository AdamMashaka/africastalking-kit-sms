import africastalking

from afri_auth.config import (
    AFRICASTALKING_USERNAME,
    AFRICASTALKING_API_KEY
)


def get_sms_client(username=None, api_key=None):

    username = username or AFRICASTALKING_USERNAME
    api_key = api_key or AFRICASTALKING_API_KEY

    if not username:
        raise ValueError(
            "AFRICASTALKING_USERNAME is missing"
        )

    if not api_key:
        raise ValueError(
            "AFRICASTALKING_API_KEY is missing"
        )

    africastalking.initialize(
        username,
        api_key
    )

    return africastalking.SMS


async def send_sms(
    phone: str,
    message: str,
    username=None,
    api_key=None
):

    sms = get_sms_client(
        username=username,
        api_key=api_key
    )

    response = sms.send(
        message,
        [phone]
    )

    return response