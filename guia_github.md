# Guia para Criar um Executável Windows usando GitHub

Este guia passo a passo vai ajudar você, como iniciante no GitHub, a criar um repositório e configurar GitHub Actions para gerar um executável Windows a partir do seu código Python.

## Parte 1: Criando uma conta no GitHub

1. **Acesse o site do GitHub**: https://github.com/
2. **Clique em "Sign up"** no canto superior direito
3. **Preencha o formulário** com:
   - Seu e-mail
   - Uma senha
   - Um nome de usuário
4. **Complete o processo de verificação** e siga as instruções na tela
5. **Escolha o plano gratuito** quando solicitado

## Parte 2: Criando um novo repositório

1. **Na página inicial do GitHub**, clique no botão verde **"New"** ou **"+"** no canto superior direito e depois em "New repository"
2. **Preencha as informações do repositório**:
   - **Nome do repositório**: `ofxcel` (ou outro nome de sua escolha)
   - **Descrição**: "Conversor de arquivos OFX para Excel"
   - **Visibilidade**: Public (para ter minutos ilimitados de GitHub Actions)
   - **Inicializar com README**: Marque esta opção
3. **Clique no botão "Create repository"**

## Parte 3: Enviando seus arquivos para o repositório

1. **Clone o repositório** para o seu computador:
   - Na página do repositório, clique no botão verde **"Code"**
   - Copie a URL HTTPS
   - No Terminal do macOS, execute:
     ```
     git clone https://github.com/SEU_USUARIO/ofxcel.git
     cd ofxcel
     ```

2. **Copie seus arquivos** para a pasta do repositório:
   - Copie todos os arquivos do seu projeto (ofxcel.py, requirements.txt, etc.)
   - Certifique-se de incluir o GUIAWindows.md e converter.bat

3. **Adicione os arquivos ao repositório**:
   ```
   git add .
   git commit -m "Primeira versão do conversor OFX para Excel"
   git push
   ```

## Parte 4: Configurando GitHub Actions

1. **No seu repositório**, clique na aba **"Actions"** no topo da página
2. **Clique no botão "set up a workflow yourself"**
3. **Você verá um editor** com um arquivo YAML. Substitua todo o conteúdo por:

```yaml
name: Build Windows Executable

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pyinstaller
        pip install -r requirements.txt
        
    - name: Build executable
      run: |
        pyinstaller --onefile --name ofxcel ofxcel.py
        
    - name: Create release package
      run: |
        mkdir release
        copy dist\ofxcel.exe release\
        copy converter.bat release\
        mkdir release\ofx
        mkdir release\excel
        copy GUIAWindows.md release\
        
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: ofxcel-windows
        path: release\
```

4. **Clique no botão "Commit changes..."** para salvar o arquivo
5. **Confirme o commit** com uma mensagem como "Adiciona workflow para criar executável Windows"

## Parte 5: Executando e Baixando o Executável

1. **Após o commit**, o GitHub Actions começará automaticamente a executar o workflow
2. **Clique na aba "Actions"** novamente para ver o progresso
3. **Clique no workflow em execução** para ver os detalhes
4. **Aguarde até que o workflow seja concluído** (status verde "completed")
5. **Na página do workflow concluído**, role para baixo até "Artifacts"
6. **Clique em "ofxcel-windows"** para baixar o arquivo ZIP com o executável

## Parte 6: Distribuindo seu Aplicativo Windows

1. **Extraia o arquivo ZIP** baixado
2. **Verifique se o pacote contém**:
   - ofxcel.exe
   - converter.bat
   - Pasta ofx (vazia)
   - Pasta excel (vazia)
   - GUIAWindows.md
3. **Teste o executável** em um computador Windows
4. **Comprima a pasta** para enviar aos usuários finais

## Dicas e Solução de Problemas

- Se o workflow falhar, verifique os logs de erro na aba Actions
- Certifique-se de que o arquivo requirements.txt inclua todas as dependências necessárias
- Se precisar fazer alterações, edite os arquivos localmente e envie novamente usando `git commit` e `git push`
- Para executar o workflow manualmente, vá para a aba Actions, selecione o workflow e clique em "Run workflow"

---

Se tiver dúvidas ou precisar de ajuda, consulte a [documentação do GitHub](https://docs.github.com/pt) ou o [Guia de GitHub Actions](https://docs.github.com/pt/actions). 