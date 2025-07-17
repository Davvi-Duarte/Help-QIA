# backend/services/test_case.py

import json
import re
from models.test_case import TestCase
from typing import List
from llm.gemini import gerar_resposta_gemini


def extract_json(text: str) -> str:
    """
    Extrai o conteúdo JSON de dentro de um bloco markdown (```json ... ```)
    """
    match = re.search(r"```json\s*(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1)
    return text  # fallback: retorna tudo se não encontrar bloco


def generate_test_cases(feature_description: str) -> List[TestCase]:
    prompt = f"""
   Você é um especialista em garantia de qualidade (QA) de software.

   Sua tarefa é gerar uma lista de CASOS DE TESTE FUNCIONAIS para validar a seguinte funcionalidade:
   
   "{feature_description}"
   
   Cada caso de teste deve conter:
   - Um identificador único (id), no formato "TC001", "TC002" etc.
   - Um título claro e objetivo
   - Uma lista de passos (steps), em ordem, que o usuário deve seguir
   - O resultado esperado ao final da execução (expected_result)
   
   Requisitos:
   - Retorne os dados exclusivamente em formato JSON puro, com esta estrutura:
   
   [
     {{
       "id": "TC001",
       "title": "Título do caso de teste",
       "steps": ["Passo 1", "Passo 2", "..."],
       "expected_result": "Resultado esperado"
     }},
     ...
   ]
   
"""

    resposta = gerar_resposta_gemini(prompt)
    json_string = extract_json(resposta)

    try:
        parsed = json.loads(json_string)
        return [TestCase(**tc) for tc in parsed]
    except Exception as e:
        return [{
            "id": "ERRO",
            "title": "Erro ao processar resposta da LLM",
            "steps": [str(e)],
            "expected_result": resposta
        }]
