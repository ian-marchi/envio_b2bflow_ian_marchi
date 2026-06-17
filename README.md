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
- SUPABASE_URL=
- SUPABASE_KEY=
- ZAPI_INSTANCE_ID=
- ZAPI_INSTANCE_TOKEN=
- ZAPI_CLIENT_TOKEN=

## Como instalar
pip install -r requirements.txt

## Como rodar
python main.py

## Adicionar novos contatos (opcional)

O projeto inclui um script interativo para cadastrar contatos direto no Supabase,
sem abrir o painel. Ele pergunta o nome e o telefone no terminal, valida o número
(somente dígitos, 12–13 com DDI) e insere na tabela `contatos`.

Para rodar:

    python add_contato.py

> Observação: o cadastro exige uma policy de INSERT no Supabase (por padrão o `anon`
> só tem permissão de leitura). Rode uma vez no SQL Editor:
>
>     create policy "insercao publica de contatos"
>     on contatos for insert to anon with check (true);