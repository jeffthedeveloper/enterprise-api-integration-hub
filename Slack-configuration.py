from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Slack Token
slack_token = 'YOUR_SLACK_TOKEN'
client = WebClient(token=slack_token)

# Carregar o modelo GPT-6JB ou GPT-2 como exemplo
model_name = 'gpt2'  # Substitua por GPT-6JB
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para gerar resposta com o modelo GPT
def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors=""pt"")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
