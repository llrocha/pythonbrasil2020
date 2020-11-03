import os
from zipcode_db import ZipCodeDB

# Load ceps
fp = open('ceps.txt')
lines = fp.readlines()
fp.close()

# Create database
zipcode_db = ZipCodeDB('./base/cep.db', create=True)

# Populate database
count = 0
for cep in lines:
    items = cep.split('\t')
    cep = items[0].strip()
    cidade, estado = items[1].split('/')
    cidade = cidade.strip()
    estado = estado.strip()

    if(len(items) >= 3):
        bairro = items[2].strip()
    else:
        bairro = None
    if(len(items) >= 4):
        logradouro = items[3].strip()
    else:
        logradouro = None
    if(len(items) >= 5):
        descricao = items[4].strip()
    else:
        descricao = None
    zipcode_db.insert(cep, cidade, estado, bairro, logradouro, descricao)
    if((count % 100) == 0):
        print('Contagem {0}\r'.format(count), end='')
    count += 1
print('Contagem {0}\r'.format(count))
zipcode_db.commit()