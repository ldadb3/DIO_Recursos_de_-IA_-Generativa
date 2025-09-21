import os
from openai import OpenAI

# Certifique-se de que a variável de ambiente OPENAI_API_KEY está configurada
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Para este exemplo, vamos simular a resposta da API.
# Em um ambiente real, você descomentaria as linhas acima e usaria a API da OpenAI.

def generate_text_example(prompt_text):
    # Simulação de uma chamada à API da OpenAI
    # Em um cenário real, a resposta viria da OpenAI
    simulated_response = {
        "choices": [
            {
                "text": f"\n\nCom base no seu prompt: '{prompt_text}', aqui está uma continuação criativa e relevante. Esta é uma demonstração de como a IA pode auxiliar na geração de conteúdo, expandindo ideias e fornecendo novas perspectivas. A qualidade da resposta depende diretamente da clareza e especificidade do prompt original."
            }
        ]
    }
    return simulated_response["choices"][0]["text"]

if __name__ == "__main__":
    prompt = "Escreva uma breve descrição para um novo aplicativo de meditação que usa sons da natureza para guiar o usuário."
    print(f"Prompt enviado: {prompt}")
    generated_content = generate_text_example(prompt)
    print(f"Conteúdo gerado:\n{generated_content}")


