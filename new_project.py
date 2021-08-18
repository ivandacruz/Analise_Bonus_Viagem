# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior de que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do youtube

# Caso não seja maior do que 55.000 não quero fazer nada

# instalar:
# Em python comando >pip install o nome da biblioteca
# pandas
# openpyxl
# twilio


import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
# ou
# Seu SID de conta do twilio.com/console
account_sid = "ACd5ddfa9d75dfe1bd415fdbbffb049b97"

# Your Auth Token from twilio.com/console
# Seu token de autenticação de twilio.com/console
auth_token  = "26ce1fc6d75bc01c6bd24cac921f63e0"
client = Client(account_sid, auth_token)


# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

# Quem (for) vai fazer o looping do código
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            # O número de telefone em questão é o número que sera enviado a mensagem e é sem traço em:
            to="+55119xxxx-xx98",
            # Esse número vai enviar a mensagem esse número é do sistema do twilio!
            from_="+18507161855",
            body=f'No mês {mes} alguem bateu a meta. vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)


