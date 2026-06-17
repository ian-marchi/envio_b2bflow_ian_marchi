import os

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



def adicionar_contato():
    client = create_client(supabase_url, supabase_key)
    print("=== Novo Contato ===")
    nome = input("Digite o nome do contato: ")
    while True:
        print("Seu contato é brasileiro: (y) / (n))")
        contato_brasil = input()
        if contato_brasil == "n":
            telefone = input("Então digite o telefone do seu contato com DDI+DDD, ex: 5511999998888\n")
            if not telefone.isdigit() or len(telefone) < 12 or len(telefone) > 13:
                print("Resposta invalida, não use simbolos especiais, somente numeros\nEntão digite o telefone do seu contato com DDI+DDD, ex: 5511999998888")
                continue
            break
        elif contato_brasil == "y":
            numero = input("Então digite o telefone do seu contato com DDD, ex: 11999998888\n")
            telefone = "55"+ numero
            if not telefone.isdigit() or len(telefone) < 12 or len(telefone) > 13:
                print("Resposta invalida, não use simbolos especiais, somente numeros\nEntão digite o telefone do seu contato com DDI+DDD, ex: 5511999998888")
                continue
            break
        else:
            print("Opção invalida, Digite o somente uma das alternativas")

    print(f"\nSucesso! Seu contato é: '{nome}' com o numero '{telefone}'!")

    response = client.table("contatos").insert({
        "nome_contato": nome,
        "telefone": telefone, 
    }).execute()

    return response.data

if __name__ == "__main__":
    adicionar_contato()