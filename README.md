# OFXCEL - Conversor de OFX para Excel

Uma ferramenta simples para converter arquivos OFX (Open Financial Exchange) para planilhas Excel.

## Instalação

1. Clone este repositório ou baixe os arquivos
2. Configure o ambiente isolado com UV:

```
chmod +x setup.sh
./setup.sh
```

O script `setup.sh` verificará se o UV está instalado e, caso não esteja, o instalará automaticamente. Em seguida, criará um ambiente virtual isolado e instalará todas as dependências necessárias.

## Uso

### Converter um único arquivo OFX:

```
python ofxcel.py caminho/para/arquivo.ofx
```

Por padrão, o arquivo Excel será criado no mesmo diretório com o mesmo nome, mas com extensão .xlsx.

### Especificar arquivo de saída:

```
python ofxcel.py caminho/para/arquivo.ofx -o caminho/para/saida.xlsx
```

### Converter todos os arquivos OFX em um diretório:

```
python ofxcel.py pasta/com/arquivos/ofx -o pasta/para/excel
```

## Estrutura do Projeto

- `ofx/` - Diretório para armazenar arquivos OFX
- `excel/` - Diretório para armazenar os arquivos Excel gerados
- `ofxcel.py` - Script principal
- `requirements.txt` - Dependências do projeto

## Exemplo de Uso com Diretórios do Projeto

Após configurar o ambiente com o script `setup.sh`, você pode usar o conversor de duas formas:

1. **Usando o script auxiliar:**
```
chmod +x converter.sh
./converter.sh
```

2. **Diretamente com o ambiente ativado:**
```
source .venv/bin/activate
python ofxcel.py ofx/ -o excel/
deactivate
```

Este comando irá processar todos os arquivos OFX na pasta `ofx/` e salvar os arquivos Excel resultantes na pasta `excel/`.