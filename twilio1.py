from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
TWILIO_PHONE_NUMBER = '+15078892232'

def fetch_sms():
    return twilio_api.messages.stream()

def send_sms(body_txt, dest_phone):
    message = twilio_api.messages \
        .create(
                body=body_txt,
                from_=TWILIO_PHONE_NUMBER,
                to=dest_phone
            )
    print(message.sid)
    return message.sid

def make_call(msg, dest_phone):
    call = twilio_api.calls \
        .create(
            twiml='<Response><Say>'+msg+'</Say></Response>',
            from_=TWILIO_PHONE_NUMBER,
            to=dest_phone   
        )
    print(call.sid)
    return call.sid