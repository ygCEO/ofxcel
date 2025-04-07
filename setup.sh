#!/bin/bash

# Verifica se o uv está instalado
if ! command -v uv &> /dev/null; then
    echo "UV não encontrado. Instalando..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Recarregar o PATH para incluir uv
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Criar ambiente virtual com uv
echo "Criando ambiente virtual com uv..."
uv venv .venv

# Ativa o ambiente virtual
source .venv/bin/activate || source .venv/Scripts/activate

# Instala as dependências com uv
echo "Instalando dependências..."
uv pip install -r requirements.txt

echo "Ambiente configurado com sucesso!"
echo "Para ativar o ambiente, use: source .venv/bin/activate"