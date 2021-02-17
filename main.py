import phonenumbers
from phonenumbers import geocoder, carrier
inp_numero = input('Número: ')
try:
    numero = phonenumbers.parse(inp_numero)
    operadora = carrier.name_for_number(numero, 'pt-br')
    regiao = geocoder.description_for_number(numero, 'pt-br')
    print(f'\n\nOperadora: {operadora}\nEstado: {regiao}')
except:
    print('\n\nAlgo deu errado.')
