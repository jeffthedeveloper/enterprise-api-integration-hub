def post_message(channel, message):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print(f""Mensagem enviada para o canal {channel}: {message}"")
    except SlackApiError as e:
        print(f""Erro ao enviar mensagem para o Slack: {e.response['error']}"")

def respond_to_slack_message(event_data):
    text = event_data['event']['text']
    channel = event_data['event']['channel']
    
    # Gerar resposta com GPT-6JB
    response = generate_response(text)
    post_message(channel, response)

# Exemplo de uso: responder quando uma nova mensagem chega
event_data = {
    'event': {
        'text': 'Qual é o tempo hoje?',
        'channel': 'YOUR_CHANNEL_ID'
    }
}
respond_to_slack_message(event_data)
