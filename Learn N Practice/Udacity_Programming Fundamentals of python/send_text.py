from twilio.rest import Client

account = "ACd1b5f2a548b2c37e0a92450certrtrte"
token = "01feea475b99a0ea33366brty6567535b"
client = Client(account, token)

message = client.messages.create(
    to="+14104934207",
    from_="+12018904657",
    body="Sorry, phone is restarting :P"
    )

print(message.sid)
