from twilio.rest import Client

account_SID = "AC656eaa23dae83cd027d80deef15de30d"
account_token = "bb8eb1e8a4f729836d65aaf603e76f38"

twillios_phn = "+12564484449"

phone_numbers = ["+919176285666", "+917824043672", "+919498811321", "+919342579245", "+919445691579"]
for my_phn in phone_numbers:
    #my_phn = "+919176285666"
    client = Client(account_SID, account_token)
    msg = client.messages.create(
    body = 'avalanche detected',
    from_=twillios_phn,
    to=my_phn
)

print("SMS sent successfully")