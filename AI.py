import apiai
import json

custommessage = 'Как дела?'
def send_message(message):
    request = apiai.ApiAI('df2d1973cb6b4ac8a319dd200dc36e3c').text_request()
    request.lang = "ru"
    request.session_id = 'session_1'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    print(response['result']['fulfillment']['speech'])

print('Your message or exit')
message = input()
while message != 'exit':
    send_message(input())
    message = input()
