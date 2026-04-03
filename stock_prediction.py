import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_prediction_data(ticker_symbol):
    try:
        # Validação de dados: Garante que o ticker é uma string válida
        if not isinstance(ticker_symbol, str) or not ticker_symbol:
            print("Erro: Ticker inválido.")
            return None

        # Baixar dados históricos de ações com tratamento de exceções
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(period='1y')

        # Verificação de response: Verifica se o DataFrame não está vazio
        if data.empty:
            print(f"Erro: Nenhum dado encontrado para o ticker {ticker_symbol}.")
            return None

        return data

    except Exception as e:
        print(f"Erro ao ligar ao Yahoo Finance: {e}")
        return None

# MANTIDO NA ÍNTEGRA: Exemplo de uso original
ticker = 'AAPL'
data = get_stock_prediction_data(ticker)

if data is not None:
    # Plotar o preço de fechamento
    data['Close'].plot()
    plt.title(f'Preço de Fechamento - {ticker}')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.show()
