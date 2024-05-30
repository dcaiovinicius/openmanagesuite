# Guia de Instalação do MySQL no Ubuntu para ambiente de desenvolvimento. 

Este guia fornece instruções passo a passo para instalar o MySQL no Ubuntu e configurar permissões de login com root.

## Instalação do MySQL

1. Abra um terminal no seu sistema Ubuntu.

2. Atualize a lista de pacotes:

    ```bash
    sudo apt update
    ```

3. Instale o servidor MySQL:

    ```bash
    sudo apt install mysql-server
    ```

4. Durante a instalação, você será solicitado a definir uma senha para a conta root do MySQL. Insira uma senha segura e confirme.

## Verificação da Instalação

1. Verifique se o serviço do MySQL está em execução:

    ```bash
    sudo systemctl status mysql
    ```

2. Se estiver em execução, você verá uma saída indicando que o serviço está ativo (running).

## Acesso ao MySQL como root

1. Para acessar o MySQL como root, execute:

    ```bash
    sudo mysql -u root -p
    ```

2. Insira a senha do usuário root do MySQL.

## Permissões de Login com Root (opcional)

Se desejar permitir login como root de qualquer host:

1. Faça login no MySQL como root:

    ```bash
    sudo mysql -u root -p
    ```

2. Execute os seguintes comandos SQL:

    ```sql
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'sua_senha' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    ```

    Substitua 'sua_senha' pela senha desejada.

## Verificação do Login como Root de Qualquer Host

Agora você pode fazer login como root de qualquer host usando:

```bash
mysql -u root -p -h localhost
