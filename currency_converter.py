import requests

def convert_currency(amount, from_currency, to_currency):
    # --- ACRÉSCIMO: Início do bloco de segurança ---
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url, timeout=10) # Timeout adicionado para evitar travamentos
        
        # Verifica se a requisição HTTP foi bem-sucedida (Status 200)
        response.raise_for_status() 
        
        data = response.json()
        
        # Validação: Verifica se a moeda de destino existe no retorno da API
        if to_currency not in data['rates']:
            print(f"Erro: Moeda '{to_currency}' não encontrada.")
            return None
            
        rate = data['rates'][to_currency]
        return amount * rate

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão/rede: {e}")
        return None
    except KeyError:
        print("Erro: Resposta da API em formato inesperado.")
        return None
    # --- MODIFICAÇÃO: Fim do bloco de segurança ---

# Exemplos originais
amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency)

# Ajuste leve apenas para evitar erro se a função retornar None
if converted_amount is not None:
    print(f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
