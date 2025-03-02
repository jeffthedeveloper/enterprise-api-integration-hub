import slack_sdk

def send_message(channel, message):
    client = slack_sdk.WebClient(token='your-slack-token')
    response = client.chat_postMessage(channel=channel, text=message)
    return response

# Exemplo de uso
response = send_message('#general', 'Hello from Python!')
print(response)
