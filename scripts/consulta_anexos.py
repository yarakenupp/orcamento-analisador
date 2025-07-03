import requests
import pandas as pd

def obter_anexos():
    url = "https://apidatalake.tesouro.gov.br/ords/sigafluxo/sb/demonstrativo"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['items'])
        return df
    else:
        raise Exception(f"Erro na requisição: {response.status_code}")
