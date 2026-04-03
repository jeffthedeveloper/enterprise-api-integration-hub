from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

# Configuração com validação de Token
slack_token = os.getenv('SLACK_TOKEN', 'YOUR_SLACK_TOKEN')

try:
    client = WebClient(token=slack_token)
    
    # Validação de conexão inicial (opcional mas recomendado)
    # client.auth_test() 

    # Carregar o modelo GPT com tratamento de erros
    model_name = 'gpt2' 
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

except Exception as e:
    print(f"Erro crítico na configuração do Slack ou IA: {e}")
    client, tokenizer, model = None, None, None

# Função para gerar resposta com validação de inputs
def generate_response(prompt):
    if not model or not tokenizer:
        return "Erro: Sistema de IA não inicializado."
    
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
