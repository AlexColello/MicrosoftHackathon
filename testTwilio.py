from dotenv import load_dotenv
print(load_dotenv())
# from utils import fetch_sms
# from utils import send_sms
import utils
sms = utils.fetch_sms()
print(sms)
x = next(sms)
baran = '+13853369470'
anjali = '+18585272410'

for x in sms:
    print(x.body)


sms_send_result = utils.send_sms("Testing", anjali)
call_result = utils.make_call("Hello! Your loved one's service dog needs your attention! Please check in on them! Also, milky toes has very milky toes.", anjali)

