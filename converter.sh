#!/bin/bash

# Verifica se o ambiente virtual existe
if [ ! -d ".venv" ]; then
    echo "Ambiente virtual não encontrado. Execute ./setup.sh primeiro."
    exit 1
fi

# Ativa o ambiente virtual
source .venv/bin/activate || source .venv/Scripts/activate

# Executa o conversor
python ofxcel.py ofx -o excel

# Desativa o ambiente virtual
deactivate

echo "Conversão concluída!"