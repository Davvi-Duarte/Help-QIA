from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

#Modelo de entrada da Requisicao
class TestCaseRequest(BaseModel):
    feature_description: str

#Modelo de um unico caso de teste
class TestCase(BaseModel):
    id: str
    title: str
    steps: List[str]
    expected_result: str

#Modelo de saida de resposta
class TestCaseResponse(BaseModel):
    test_cases: List[TestCase]


@app.post("/generate/test-cases", response_model=TestCaseResponse)
def gerador_casos_de_teste(request: TestCaseRequest):
    descricao_feature = request.feature_description
    
    casos_de_teste = [
        TestCase(
            id="TC001",
            title="Login com credenciais válidas",
            steps=[
                "Abrir a página de login",
                "Inserir email válido e senha válida",
                "Clicar em 'Entrar'"
            ],
            expected_result="Usuário é redirecionado para o painel principal"
        ),
        TestCase(
            id="TC002",
            title="Login com senha incorreta",
            steps=[
                "Abrir a página de login",
                "Inserir email válido e senha inválida",
                "Clicar em 'Entrar'"
            ],
            expected_result="Sistema exibe mensagem de erro 'Credenciais inválidas'"
        )
    ]

    return TestCaseResponse(test_cases=casos_de_teste)

