def post_message(channel, message):
    try:
        # Verificação de response da requisição
        response = client.chat_postMessage(channel=channel, text=message)
        if response["ok"]:
            print(f"Mensagem enviada para o canal {channel}: {message}")
    except SlackApiError as e:
        print(f"Erro ao enviar mensagem para o Slack: {e.response['error']}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def respond_to_slack_message(event_data):
    try:
        # Validação de dados: Verifica se as chaves existem no evento
        if 'event' in event_data and 'text' in event_data['event']:
            text = event_data['event']['text']
            channel = event_data['event']['channel']
            
            # Gerar resposta
            response = generate_response(text)
            post_message(channel, response)
        else:
            print("Erro: Estrutura de evento inválida.")
    except Exception as e:
        print(f"Erro ao processar mensagem do Slack: {e}")

# MANTIDO NA ÍNTEGRA: Exemplo de uso original
event_data = {
    'event': {
        'text': 'Qual é o tempo hoje?',
        'channel': 'YOUR_CHANNEL_ID'
    }
}
respond_to_slack_message(event_data)
