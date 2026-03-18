# Gestor de Notas Acadêmicas

Projeto desenvolvido em Python com o objetivo de gerenciar notas acadêmicas de forma simples e organizada, separando dados entre **escola** e **faculdade**.

Permite cadastrar disciplinas, inserir notas e acompanhar o desempenho do aluno.


## Funcionalidades

### Escola
- Cadastro de disciplinas
- Inserção de até **4 notas**
- Cálculo automático da média
- Exibição da situação 


### Faculdade
- Cadastro de disciplinas
- Inserção de até **3 notas**
- Cálculo automático da média
- Exibição da situação


## Características do Projeto

- Interface feita com Tkinter
- Separação de dados entre escola e faculdade
- Cálculo dinâmico (não armazena média nem status)
- Validação de entrada (notas de 0 a 10)
- Estrutura modular:
  - `ui/` → telas
  - `data/` → gerenciamento de dados
  - `logic/` → regras do sistema


## Armazenamento

Os dados são armazenados em um arquivo JSON no formato:
``` 
`json`
{
  "escola": [],
  "faculdade": []
}
```


## Tecnologias Utilizadas

### Bibliotecas externas:
- Pillow

### Bibliotecas padrão do Python:
- tkinter
- json
- pathlib
- sys


## 📦 Como executar

1. Acesse a pasta do projeto
cd caminho/do/projeto

2. Instale as dependências:
pip install -r requirements.txt

3. Execute o projeto
python  main.py

## Observações
- Não é necessário instalar as bibliotecas padrão do Python.
- Recomenda-se o uso de ambiente virtual (venv).
- O projeto reutiliza partes de código de outro projeto, podendo haver semelhanças.
- Caso ocorra algum erro ao iniciar, execute novamente.
- Não esqueça de instalar o Pillow
