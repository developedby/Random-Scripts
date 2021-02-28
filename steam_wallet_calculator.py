"""
Calcula quanto dinheiro foi gasto na steam.
Não totalmente preciso.
Assume que é tudo em BRL e tem 0 de dinheiro na wallet no momento.
Assume que a página tá em ingles.

Para rodar:
    Salvar o HTML da página "Purchase History" em um arquivo
    (Barra Superior -> Seu Display Name -> "Account Details" -> "View Purchase History" -> Right Click -> "View Source...")
    Colocar o caminho ate esse arquivo na variavel FILE_PATH
    Rodar

Requer python >= 3.7 e BeautifulSoup4
"""
import pathlib
from datetime import datetime
from bs4 import BeautifulSoup

FILE_PATH = './transaction_history.html'
SHOW_WARNINGS = True

with open(FILE_PATH) as f:
    bs = BeautifulSoup(f.read(), 'html.parser')

entries = bs.find_all(class_="wallet_table_row")

total_spent = 0
total_market = 0
for entry in entries:
    type_ = list(entry.find_all(class_="wht_type")[0].children)[1].string.strip()

    total_tag = entry.find_all(class_='wht_total')[0]
    # Se tem filhos o primeiro tem o preço
    if len(list(total_tag.children)) > 1:
        price = list(total_tag.children)[1].string.strip()
    # Se não ta direto na string
    else:
        price = total_tag.string.strip()
    price = price.replace('R$ ', '').replace(',', '.')

    if type_ in ["Purchase", "Gift Purchase"]:
        try:
            total_spent += float(price)
        except ValueError:
            if SHOW_WARNINGS:
                print(f"WARNING: Não conseguiu processar o preço '{price}'")
    elif type_ == "Refund":
        total_spent += float(price)
    elif type_ in ["Market Transactions", "Market Transaction"]:
        wallet_change = entry.find_all(class_="wht_wallet_change")[0].string\
            .strip().replace('R$ ', '').replace(',', '.')
        total_spent -= float(wallet_change)
        total_market += float(wallet_change)

last_entry = list(entries)[-1]
date_start = last_entry.find_all(class_="wht_date")[0].string.strip()
date_start = datetime.strptime(date_start, '%d %b, %Y')
time_passed = datetime.now() - date_start
spent_per_day = total_spent / time_passed.days

print(f"Total gasto na steam: R$ {total_spent:.2f}")
print(f"Total ganhado no Market: R$ {total_market:.2f}")
print(f"Quantidade gasta por dia (desde a primeira transação): R$ {spent_per_day:.2f}")
