import requests
import pandas as pd
import os

# Garante que a pasta 'consolidados/' existe
os.makedirs("consolidados", exist_ok=True)

# URL correta da API do SICONFI
url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/anexos-relatorios"

# Faz a requisição
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    registros = data.get("items", [])
    
    # Converte em DataFrame
    df = pd.DataFrame(registros)
    
    # Salva em CSV
    df.to_csv("consolidados/anexos_relatorios.csv", index=False)
    print("✅ Arquivo salvo com sucesso em consolidados/anexos_relatorios.csv")
else:
    print(f"❌ Erro ao consultar a API. Status code: {response.status_code}")
