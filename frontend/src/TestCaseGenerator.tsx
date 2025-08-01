import { useState } from "react";
import { Button, Input, Textarea, Card } from "@shadcn/ui"; // Importa os componentes da biblioteca

const TestCaseGenerator = () => {
  const [description, setDescription] = useState<string>("");
  const [testCases, setTestCases] = useState<any[]>([]);

  const handleGenerate = async () => {
    try {
      const response = await fetch("http://localhost:8000/generate/test-cases", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ feature_description: description }),
      });
      const data = await response.json();
      setTestCases(data.test_cases);
    } catch (error) {
      console.error("Erro ao gerar casos de teste", error);
    }
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-4xl font-semibold text-primary mb-6">Gerador de Casos de Teste</h1>
      
      <Card className="bg-white p-6 rounded-lg shadow-lg">
        <Textarea
          placeholder="Descreva a funcionalidade que você deseja testar"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="mb-4 w-full p-4 border-2 border-primary rounded-lg"
        />
        <Button
          onClick={handleGenerate}
          className="w-full py-3 bg-primary text-white rounded-lg hover:bg-blue-600 transition"
        >
          Gerar Casos de Teste
        </Button>
      </Card>

      {/* Casos de teste gerados */}
      <div className="mt-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {testCases.map((testCase, index) => (
          <Card key={index} className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
            <h2 className="text-2xl font-semibold text-secondary">{testCase.title}</h2>
            <p className="mt-4 text-sm text-gray-500">Passos:</p>
            <ul className="list-disc pl-5 text-gray-700">
              {testCase.steps.map((step: string, idx: number) => (
                <li key={idx}>{step}</li>
              ))}
            </ul>
            <p className="mt-4 text-sm text-gray-500">
              <strong>Resultado esperado:</strong> {testCase.expected_result}
            </p>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default TestCaseGenerator;
