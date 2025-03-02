import yfinance as yf
import matplotlib.pyplot as plt

# Baixar dados históricos de ações
stock = yf.Ticker('AAPL')
data = stock.history(period='1y')

# Plotar o preço de fechamento
data['Close'].plot()
plt.title('Preço de Fechamento - AAPL')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.show()
