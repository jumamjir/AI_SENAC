# 29. Escreva uma função valida_email que receba um email e retorne True se for um
# formato válido e False caso contrário.

import re

def valida_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None


print(valida_email("exemplo@dominio.com"))
print(valida_email("exemplo@dominio"))
print(valida_email("exemplo@.com"))
print(valida_email("exemplo@dominio.c"))
