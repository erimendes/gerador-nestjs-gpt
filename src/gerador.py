import os
from openai import OpenAI
import re

# Configura API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lê o prompt do arquivo
with open("prompts/nest_tasks.prompt", "r", encoding="utf-8") as f:
    prompt = f.read()

# Chama a API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

texto = response.choices[0].message.content

# Extrai os blocos "Arquivo: caminho\n```codigo```"
matches = re.findall(r"Arquivo: (.+?)\n```(?:[\s\S]*?)\n([\s\S]*?)```", texto)

# Salva cada arquivo
for caminho, conteudo in matches:
    pasta = os.path.dirname(caminho)
    os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"✅ Arquivo salvo: {caminho}")

print("\n🎉 Projeto NestJS completo gerado!")
