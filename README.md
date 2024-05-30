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

### Instalação das Dependências

```bash
# Instale o Makefile
sudo apt update && sudo apt install make

# O Ubuntu já vem com uma versão de Python 3 instalada, mas você precisa criar um alias de python3 para python
echo alias python=python3 >> ~/.bashrc

# Clone o projeto
git clone https://github.com/dcaiovinicius/openmanagesuite

# Acesse a pasta do projeto
cd openmanagesuite

# Abra com seu editor de código favorito
code .
```

```text
# Você precisa criar um arquivo de configuração do projeto com o nome .env e definir o usuário e senha do MySQL

Conteúdo do arquivo .env:

FLASK_ENV=development
SECRET_KEY=vGfEX7U1FxNXoPlKiNvH2JyudoPkQJHhu4Fs3Nf6UnA=
DATABASE_URL=mysql+pymysql://root:password@localhost/mvp
```

```bash
# Criar o usuário admin
make seeds

# Iniciar o servidor HTTP de desenvolvimento
make run
```
