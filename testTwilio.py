from dotenv import load_dotenv
print(load_dotenv())
# from twilio import fetch_sms
# from twilio import send_sms
import twilio_api
sms = twilio_api.fetch_sms()
print(sms)
x = next(sms)
baran = '+13853369470'
anjali = '+18585272410'

for x in sms:
    print(x.body)


sms_send_result = twilio_api.send_sms("Testing", anjali)
call_result = twilio_api.make_call("Hello! Your loved one's service dog is trying to get your attention! Please check in on them!", anjali)

