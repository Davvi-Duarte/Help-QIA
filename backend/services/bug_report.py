# backend/services/test_case.py
import json
import re
from models.bug_report import BugReport
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


def generate_bug_report(bug_description: str) -> BugReport:
    prompt = f"""
Você é um engenheiro de QA sênior especializado em análise de defeitos e qualidade de software.

Sua tarefa é gerar um RELATÓRIO DE BUG completo, no formato JSON, baseado na seguinte descrição de comportamento defeituoso do sistema:

"{bug_description}"

O relatório deve conter os seguintes campos obrigatórios:

- id: string com identificador (ex: "BUG-001")
- title: título claro e objetivo do bug
- environment: detalhes do ambiente de teste (ex: navegador, SO, versão do app)
- steps_to_reproduce: lista ordenada dos passos para reproduzir o bug
- actual_result: o que acontece de errado
- expected_result: o que deveria acontecer
- severity: nível de severidade (ex: Crítico, Alto, Médio, Baixo)
- priority: prioridade de correção (ex: Alta, Média, Baixa)
- evidence: prints, mensagens de erro, ou logs relevantes
- notes: observações adicionais, intermitência ou workaround

Retorne **apenas JSON válido** no seguinte formato:

{{
  "id": "BUG-001",
  "title": "Erro 500 ao tentar salvar formulário sem e-mail",
  "environment": "Windows 11 / Chrome 125.0 / Staging",
  "steps_to_reproduce": [
    "Acessar a página de cadastro",
    "Preencher todos os campos, exceto o e-mail",
    "Clicar em 'Salvar'"
  ],
  "actual_result": "Erro 500 exibido e formulário não salvo",
  "expected_result": "Sistema deve exibir mensagem de validação para o campo e-mail",
  "severity": "Alto",
  "priority": "Alta",
  "evidence": "Screenshot anexo mostrando o erro 500",
  "notes": "Erro ocorre 100% das vezes; sem contorno possível"
}}
"""

    resposta = gerar_resposta_gemini(prompt)
    json_string = extract_json(resposta)

    try:
        parsed = json.loads(json_string)
        return BugReport(**parsed)
    except Exception as e:
        return BugReport(
            id="BUG-ERROR",
            title="Erro ao processar resposta da LLM",
            environment="Desconhecido",
            steps_to_reproduce=[],
            actual_result=str(e),
            expected_result=resposta,
            severity="Alto",
            priority="Alta",
            evidence=None,
            notes="Erro ao converter JSON"
        )
