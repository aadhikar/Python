from twilio.rest import Client

account = "ACd1b5f2a548b2c37e0a92450ce611860e"
token = "01feea475b99a0ea33366b4d451cb35b"
client = Client(account, token)

message = client.messages.create(
    to="+14104934207",
    from_="+12018904657",
    body="Sorry, phone is restarting :P"
    )

print(message.sid)
