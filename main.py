import requests

print('~' * 42)
print(f'{"Consulta CEP - ViaCEP":^42}')
print('~' * 42)
cep_option = ''

# Verificação do CEP
while not cep_option.isdecimal() or not len(cep_option) == 8:
    cep_option = input('CEP a ser consultado (8 dígitos)> ')
    if cep_option.isdecimal() is False or len(cep_option) != 8:
        print(f'\033[31mO CEP informado ({cep_option}) é inválido!\033[m')

# Consumo da API
consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_option}/json/')
cep_data = consumo_api.json()
print(cep_data)

# Organização das informações
print('~' * 42)
