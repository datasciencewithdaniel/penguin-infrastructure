# import json
import os

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

DISCORD_BABY_PENGUIN_PUBLIC_KEY = os.getenv("DISCORD_BABY_PENGUIN_PUBLIC_KEY")
RESPONSE_TYPES = {
    "PONG": 1,
    "ACK_NO_SOURCE": 2,
    "MESSAGE_NO_SOURCE": 3,
    "MESSAGE_WITH_SOURCE": 4,
    "ACK_WITH_SOURCE": 5,
}


def verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event["params"]["header"].get("x-signature-ed25519")
    auth_ts = event["params"]["header"].get("x-signature-timestamp")

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(DISCORD_BABY_PENGUIN_PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig))  # raises an error if unequal


def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False


def lambda_handler(event, context):

    try:
        verify_signature(event)
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")

    # returns the pong to a ping event
    body = event.get("body-json")
    if ping_pong(body):
        return {"type": 1}

    return {
        "type": RESPONSE_TYPES["MESSAGE_NO_SOURCE"],
        "data": {
            "tts": False,
            "content": "Yes My Emperor",
            "embeds": [],
            "allowed_mentions": [],
        },
    }

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from the Emperor')
    # }
