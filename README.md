Aqui vai um README pensado para alguém sem experiência técnica conseguir rodar seu script sem dor de cabeça:

---

# 📊 PNAD Contínua – Extração de Dados (UF 26)

Este projeto baixa automaticamente os microdados da PNAD Contínua (IBGE), extrai os arquivos e gera um CSV filtrado apenas para o estado de Pernambuco (UF = 26).

---

## 🧾 O que esse programa faz?

* Baixa dados do IBGE (anos de 2023 a 2025)
* Extrai os arquivos compactados (.zip)
* Lê os dados em formato texto
* Filtra apenas registros da UF 26 (Pernambuco)
* Gera um arquivo final:
  **`pnad_2023_2025_resumo.csv`**

---

## ⚙️ Requisitos

Antes de começar, você precisa instalar:

### 1. Instalar o Python

* Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Clique em **Download Python**
* Durante a instalação:

  * ✅ Marque a opção **"Add Python to PATH"**
  * Clique em **Install Now**

---

## 📥 Passo 1 – Baixar o código

1. Copie o código fornecido
2. Abra o **Bloco de Notas**
3. Cole o código
4. Salve o arquivo como:

```
pnad_script.py
```

⚠️ Importante:
No campo "Tipo", escolha **Todos os arquivos** para não salvar como `.txt`

---

## 📁 Passo 2 – Criar uma pasta para o projeto

1. Crie uma pasta, por exemplo:

```
C:\pnad_projeto
```

2. Coloque o arquivo `pnad_script.py` dentro dela

---

## 🧪 Passo 3 – Criar um ambiente virtual

Isso evita problemas com dependências. Se não desejar criar um ambiente virtual e instalar as bibliotecas Pandas e Requests direto no ambiente global, pule para o passo 4. Se já tiver ass biblioteca Pandas e Requests no ambiente global, pule para o passo 5.

### No Windows:

1. Abra o Prompt de Comando:

   * Aperte `Win + R`
   * Digite `cmd` e pressione Enter

2. Vá até a pasta do projeto:

```
cd C:\pnad_projeto
```

3. Crie o ambiente virtual:

```
python -m venv venv
```

4. Ative o ambiente:

```
venv\Scripts\activate
```

Se deu certo, aparecerá `(venv)` no início da linha.

---

## 📦 Passo 4 – Instalar as bibliotecas necessárias

Digite:

```
pip install pandas requests
```

---

## ▶️ Passo 5 – Rodar o programa

Execute:

```
python pnad_script.py
```

---

## ⏳ O que esperar

* O programa começará a baixar os dados
* Pode demorar alguns minutos (os arquivos são grandes)
* Você verá mensagens como:

```
Baixando 2023 T1...
Baixando 2023 T2...
...
```

---

## 📄 Resultado final

Após terminar, aparecerá a mensagem "Arquivo final gerado!" e será criado o arquivo:

```
pnad_2023_2025_resumo.csv
```

Esse arquivo estará dentro da pasta do projeto.

Se quiser abrir o CSV:
* Use o Excel
* Ou o LibreOffice Calc


