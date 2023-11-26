from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACbe191d968140e8c261494b16b18ad04d'
TWILIO_AUTH_TOKEN = '3453bacea672e48c8ee4a5b875fb71ba'
def send_text():
  client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN )
  message = client.messages.create(
  to= str('+13156403233'),
  from_="+13156403238", # insert trial number
  body="Hey I hope you received this message") # insert message
send_text.short_description = "Send text campaign"

send_text()