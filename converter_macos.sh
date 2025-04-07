#!/bin/bash

echo "===== Conversor OFX para Excel ====="
echo ""
echo "Convertendo arquivos OFX para Excel..."
echo ""

# Ativa o ambiente virtual (se existir)
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Executa o conversor Python
python ofxcel.py ofx -o excel

# Desativa o ambiente virtual (se foi ativado)
if [ -d ".venv" ]; then
    deactivate
fi

echo ""
echo "Conversão concluída!"
echo "Os arquivos Excel estão disponíveis na pasta 'excel'"
echo ""
read -p "Pressione ENTER para continuar..." 