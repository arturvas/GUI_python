import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-USD')

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCUSD']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto



janela = Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry()

# texto dentro da janela, e dentro coloca qual janela pertence o texto
texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas')
# agora dizemos onde ficara o texto
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Cotações [USD/EUR/BTC]', command=pegar_cotacoes) # obs.: nao passar o comando com a funcao com parentes
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()