![Logo do Projeto](static/assets/logo.png)

# Plataforma Open Source e Self-Host para Gestão de Negócios | FCARP

Uma plataforma open source e self-host definitiva para a gestão de negócios, projetada para oferecer controle total sobre suas operações. Com um foco inicial no gerenciamento de inventário e controle de estoque

Nosso objetivo é iniciar o desenvolvimento deste software com foco no gerenciamento de inventário e controle de estoque.


![Logo do Projeto](static/assets/screenshot.png)


## Instalação para Ambiente de Desenvolvimento

## Requisitos

- Ubuntu
- MySQL
- Python 3
- Makefile

### Instalação das Dependências e ferramnetas para desenvolvimento

```bash
# Instale o Makefile e o git
sudo apt update && sudo apt install make git

# Clone o projeto
git clone https://github.com/dcaiovinicius/openmanagesuite

# Acesse a pasta do projeto
cd openmanagesuite

# Abra com seu editor de código favorito
code .


# Você precisa renomear um arquivo de configuração do projeto de .env-development para .env e definir o usuário e senha do MySQL.
```

```bash
# instale as dependências
make

# Criar o usuário admin
make seeds

# Iniciar o servidor HTTP de desenvolvimento
make run
```
