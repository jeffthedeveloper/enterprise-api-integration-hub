import tweepy
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Configuração do Twitter
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Carregar o modelo GPT-6JB ou GPT-2 como um exemplo
model_name = 'gpt2'  # Substitua pelo modelo GPT-6JB
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para gerar resposta com o modelo GPT
def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors=""pt"")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
