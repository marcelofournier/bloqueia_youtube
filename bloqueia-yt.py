import os

"""
O objetivo deste programa é simples: bloquear o acesso ao youtube
pelo navegador web, quando acessado via url
Apesar de ternicamente ter um solução bastante simples, pode ser muito útil
tanto em ambientes empresariais como domésticos.
"""


# Caminho do arquivo hosts
hosts_path = '/etc/hosts'

# IP inválido para redirecionamento
redirect_ip = '127.0.0.1'

# Lista de sites a serem bloqueados
sites_to_block = ['www.youtube.com', 'youtube.com']

def block_websites():
    try:
        # Abre o arquivo hosts em modo de escrita
        with open(hosts_path, 'a') as file:
            for site in sites_to_block:
                # Escreve no arquivo hosts o redirecionamento do site para o IP inválido
                file.write(f'{redirect_ip} {site}\n')
        print('Sites bloqueados com sucesso!')
    except Exception as e:
        print(f'Erro ao bloquear sites: {e}')

if __name__ == '__main__':
    # Verifica se o usuário tem permissão de superusuário (root)
    if os.geteuid() == 0:
        block_websites()
    else:
        print('Este programa precisa ser executado com permissões de superusuário (root).')
