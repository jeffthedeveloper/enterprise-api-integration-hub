import slack_sdk
from slack_sdk.errors import SlackApiError

def send_message(channel, message):
    try:
        # Adicionado timeout e tratamento de erros
        client = slack_sdk.WebClient(token='your-slack-token', timeout=15)
        response = client.chat_postMessage(channel=channel, text=message)
        return response
    except SlackApiError as e:
        print(f"Erro na API do Slack: {e.response['error']}")
        return None
    except Exception as e:
        print(f"Erro de ligação: {e}")
        return None

# MANTIDO NA ÍNTEGRA: Exemplo de uso original
response = send_message('#general', 'Hello from Python!')
if response:
    print(response)
