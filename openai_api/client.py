import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

api_key = os.getenv('SUA_CHAVE_DE_API_AQUI')

client = None
if api_key:
    client = OpenAI(api_key=api_key)

def get_car_ai_bio(model, brand, year):

    if not client:
        return 'Descrição automática não disponível.'

    prompt = f'''
    Crie uma descrição detalhada para um carro usado.

    Marca: {brand}
    Modelo: {model}
    Ano: {year}

    A descrição deve ser atrativa para um site de venda de carros usados.
    '''

    response = client.responses.create(
        model='gpt-4.1-mini',
        input=prompt
    )

    return response.output_text
