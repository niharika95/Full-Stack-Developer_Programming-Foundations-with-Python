from twilio.rest import TwilioRestClient

account_sid = "ACdbf58bd631fcf4ed808b6d90a14b25d4" # Your Account SID from www.twilio.com/console
auth_token  = "2b732f8a114a22146d5c32558f8a0142"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	body="Tissssuuuuueeeee!!!",
    to="+919769148551",    # Replace with your phone number
    from_="+13472692256") # Replace with your Twilio number

print(message.sid)