import os

# Caminho do arquivo hosts
hosts_path = '/etc/hosts'

# Lista de sites a serem desbloqueados
sites_to_unblock = ['www.youtube.com', 'youtube.com']

def unblock_websites():
    try:
        # Abre o arquivo hosts em modo de leitura
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        
        # Abre o arquivo hosts em modo de escrita
        with open(hosts_path, 'w') as file:
            for line in lines:
                # Escreve no arquivo hosts todas as linhas, exceto as que bloqueiam os sites
                if not any(site in line for site in sites_to_unblock):
                    file.write(line)
        print('Sites desbloqueados com sucesso!')
    except Exception as e:
        print(f'Erro ao desbloquear sites: {e}')

if __name__ == '__main__':
    # Verifica se o usuário tem permissão de superusuário (root)
    if os.geteuid() == 0:
        unblock_websites()
    else:
        print('Este programa precisa ser executado com permissões de superusuário (root).')
