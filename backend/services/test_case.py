# backend/services/test_case.py
from models.test_case import TestCase

def generate_mock_test_cases(feature_description: str):
    return [
        TestCase(
            id="TC001",
            title=f"Verificar comportamento ao {feature_description}",
            steps=[
                "Acessar o sistema",
                f"Executar ação: {feature_description}",
                "Verificar resultado esperado"
            ],
            expected_result="Usuário é redirecionado para o painel principal"
        )
    ]
