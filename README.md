# Envio de mensagens com Supabase e Z-API

## O que o projeto faz
Lê contatos cadastrados no Supabase e envia via Z-API a mensagem:
"Olá, <nome_contato> tudo bem com você?"

## Setup da tabela
Tabela: contatos

Campos:
- id
- nome_contato
- telefone
- ativo
- created_at

## Variáveis de ambiente
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_INSTANCE_TOKEN=
ZAPI_CLIENT_TOKEN=

## Como instalar
pip install -r requirements.txt

## Como rodar
python main.py
