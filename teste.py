import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC51972a5b9be8b1de294be2cd1320f890"
# Your Auth Token from twilio.com/console
auth_token = "3dfc061ff411f0e81fa3910548312e03"
client = Client(account_sid, auth_token)


# PROGRAMMING LOGIC

# 1 - Open the six Excel files sent by your boss 
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# For each file: - 2 Check if any value under 'Vendas' column is higher than 55,000

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # 3 If there's a value higher than 55,000 -> Send a text message with the employee name and the value of sales

    if (tabela_vendas['Vendas'] > 55000).any(): # any() para consultar se algum valor é maior que 55, não a quantidadde de linhas na tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguém bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')
        message=client.messages.create(
                to="+610451044332",
                from_="+12568297369",
                body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# If there's no value above 55,000 don't send any message.

