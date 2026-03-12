# 🔑 Gerador de Chaves Hexadecimais em Python

Este projeto é um **gerador de chaves hexadecimais** feito em Python que também salva as chaves em um **banco de dados SQLite**.

## 📌 Funcionalidades

* Gerar chaves hexadecimais seguras
* Armazenar chaves em banco de dados
* Listar chaves salvas
* Banco de dados local usando SQLite

## 🛠️ Tecnologias

* Python 3
* SQLite
* Biblioteca `secrets`

## 📂 Estrutura do Projeto

```
projeto/
├── main.py
```

## ⚙️ Instalação

1. Clone o repositório:

```
git clone https://github.com/jovigod888/gerador-de-senhas.git
```

2. Entre na pasta do projeto:

```
cd gerador-de-senhas.git
```

3. Execute o programa:

```
python main.py
```

## 🔐 Exemplo de chave gerada

```
9f4a8c2d7b1e4f3a6c8d0b1e2f3a4c5d
```

## 📚 Como funciona

O projeto usa a biblioteca `secrets` do Python para gerar chaves seguras e armazena essas chaves em um banco de dados SQLite usando `sqlite3`.

## 🚀 Possíveis melhorias

* Criar API com Flask ou FastAPI
* Interface web
* Sistema de autenticação
* Verificação de chave usada

## 👨‍💻 Autor

Desenvolvido por **Jovigod888**
