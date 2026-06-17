import logging
import os

import requests
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

def getenv_detect(nome: str) -> str:
    valor = os.getenv(nome)
    if valor is None:
        raise RuntimeError(f"Variavel ' {nome}' nao foi definida no .env")
    return valor


supabase_url = getenv_detect("SUPABASE_URL")
supabase_key = getenv_detect("SUPABASE_KEY")

zapi_instance_id = getenv_detect("ZAPI_INSTANCE_ID")
zapi_instance_token = getenv_detect("ZAPI_INSTANCE_TOKEN")
zapi_client_token = getenv_detect("ZAPI_CLIENT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def buscar_contatos():
    client = create_client(supabase_url, supabase_key)
    response = client.table("contatos").select("*").limit(3).execute()

    return response.data


def enviar_mensagem(telefone, mensagem):
    url = f"https://api.z-api.io/instances/{zapi_instance_id}/token/{zapi_instance_token}/send-text"
    envio = requests.post(
        url,
        json={"phone": telefone, "message": mensagem},
        headers={"Client-Token": zapi_client_token},
    )

    return envio


def main():
    contatos = buscar_contatos()

    logging.info(f"{len(contatos)} contatos encontrados. Iniciando envios...")
    for contato in contatos:
        nome = contato["nome_contato"]
        telefone = contato["telefone"]

        mensagem = f"Olá, {nome} tudo bem com você?"

        try:
            resposta = enviar_mensagem(telefone, mensagem)
            if resposta.status_code in (200,201):
                logging.info(f"Mensagem enviada para {nome} com o numero: {telefone}")
            else:
                logging.error(f"Falha ao enviar mensagem para {nome}: \n{resposta.status_code} : {resposta.text}")
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem para {nome}: {e}")

if __name__ == "__main__":
    main()