import requests
import pandas as pd

# Endpoint base da API
url = "https://apidatalake.tesouro.gov.br/ords/sigafluxo/sb/v_despesa_execucao"

# Parâmetros de consulta
params = {
    "q": "acao=0Z50",  # filtra pela ação da DRU
    "limit": 10000     # aumenta limite de registros por página
}

# Faz a requisição GET
response = requests.get(url, params=params)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    try:
        data = response.json()
        registros = data.get("items", [])
        if not registros:
            print("⚠️ Nenhum dado encontrado na resposta da API.")
        else:
            # Converte para DataFrame
            df = pd.DataFrame(registros)

            # Converte valores monetários para numérico
            for col in ["valor_empenhado", "valor_liquidado", "valor_pago"]:
                df[col] = pd.to_numeric(df[col], errors="coerce")

            # Salva o CSV final
            df.to_csv("consolidados/dru_consolidado.csv", index=False)
            print("✅ Arquivo salvo com sucesso em consolidados/dru_consolidado.csv")
    except ValueError:
        print("❌ Erro ao decodificar JSON. Conteúdo da resposta:")
        print(response.text)
else:
    print(f"❌ Erro na requisição: status {response.status_code}")
    print("Resposta da API:")
    print(response.text)
