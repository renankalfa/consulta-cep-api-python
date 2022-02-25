import requests
from time import sleep


def main():
    print('=' * 42)
    print(f'          \033[46mConsulta CEP - ViaCEP\033[m')
    print('=' * 42)
    cep_option = ''

    # Verificação do CEP
    while not cep_option.isdecimal() or not len(cep_option) == 8:
        cep_option = input('\033[36mCEP a ser consultado (8 dígitos)>\033[m ')
        if cep_option.isdecimal() is False or len(cep_option) != 8:
            print(f'\033[31mO CEP informado ({cep_option}) é inválido!\033[m')

    # Consumo da API
    consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_option}/json/')
    cep_data = consumo_api.json()

    # Organização das informações
    sleep(0.5)
    print('=' * 42)
    if 'erro' not in cep_data.keys():
        sleep(0.5)
        print(f'\033[46mCEP consultado:\033[m \033[36m{cep_data["cep"]}\033[m')
        sleep(0.5)
        print(f'\033[43mEndereço:      \033[m \033[33m{cep_data["logradouro"]} {cep_data["complemento"]}\033[m')
        sleep(0.5)
        print(f'\033[42mLocalidade/UF: \033[m \033[32m{cep_data["localidade"]}-{cep_data["uf"]}\033[m')
        sleep(2)
    else:       # 01001000
        print(f'\033[31mCEP {cep_option} inválido!\033[m')
    print('=' * 42)
    sleep(0.5)
    user_option = input('Deseja consultar outro CEP [S/N]? ').upper()
    while user_option not in 'SN':
        print(f'\033[31mErro! {user_option} é inválido!\033[m')
        user_option = input('Deseja consultar outro CEP [S/N]? ').upper()
    if user_option.upper() == 'S':
        print('\n' * 100)
        main()
    else:
        print('\033[31mEncerrando o programa\033[m', end='')
        for c in range(3):
            sleep(0.5)
            print('\033[31m.\033[m', end='')
        print()


if __name__ == '__main__':
    main()
