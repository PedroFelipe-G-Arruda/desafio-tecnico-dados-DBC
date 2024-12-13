## Desafio Técnico de Engenharia de Dados - DBC

### **Objetivo do Projeto**
Este projeto foi desenvolvido como parte de um desafio técnico, com o objetivo de demonstrar habilidades na construção de pipelines de dados e manipulação de informações utilizando Python, PySpark e MySQL.

---

### **Design do Projeto**
#### Estrutura Geral
- **MySQL**: Banco de dados relacional utilizado para armazenar as tabelas necessárias para o desafio.
- **PySpark**: Utilizado para realizar a extração, transformação e carga (ETL) dos dados, além de realizar integrações com o MySQL.
- **Scripts em Python**: Responsáveis pela geração de dados, inserção no banco e execução do pipeline ETL.
- **CSV**: Resultado final do pipeline, exportado no formato delimitado por `|`.

#### Estrutura de Diretórios
```
desafio-tecnico-dados-DBC/
│
├── README.md                   # Documentação principal
├── tabelas.md                  # Documentação da criação do banco de dados e tabelas
├── gerar_dados.py              # Script Python para gerar e inserir dados no MySQL
├── main.py                     # Script principal do ETL com PySpark
├── mysql-connector-j-9.1.0.jar # Conector MySQL 
│
├── output/              # Diretório de saída para os arquivos CSV
│   └── movimento_flat.csv
│
└── env/                 # Ambiente virtual (não incluso no repositório)
```

---

### **Decisões de Design**
1. **Uso de PySpark**: Escolhido por sua capacidade de processamento em larga escala, permitindo futuras expansões para volumes maiores de dados.
2. **MySQL**: Banco relacional amplamente utilizado e confiável para armazenar dados estruturados.
3. **Separação de Scripts**: Cada etapa do projeto (criação de tabelas, geração de dados, pipeline ETL) foi isolada para garantir modularidade e facilitar a manutenção.

---

### **Dificuldades Encontradas**
1. **Configuração de Ambientes**: Houve desafios para configurar corretamente o ambiente no Windows, especialmente com o PySpark e dependências externas.
2. **Gerenciamento de Arquivos CSV**: Problemas iniciais com codificação de caracteres (UTF-8) e separador de campos no CSV.
3. **Erro de Links Nativos no Hadoop**: Ocorreu um erro relacionado ao `NativeIO` no Windows durante o salvamento do arquivo, mas foi contornado utilizando permissões corretas e ajustando o ambiente.

---

### **O que faria se tivesse mais tempo**
1. **Automatização de Deploy**:
   - Usaria ferramentas como Docker para encapsular o ambiente.
2. **Documentação Avançada**:
   - Melhoraria os comentários nos scripts e adicionaria documentação detalhada das funções.
3. **Visualizações e Relatórios**:
   - Melhoraria a organização do projeto
4. **Visualizações e Relatórios**:
   - Adicionaria um componente para análise visual dos dados (exemplo: Power BI ou Dash).

---

### **Como Executar**
1. **Configurar o Ambiente Virtual**:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # No Windows
   pip install -r requirements.txt
   ```

2. **Criar as Tabelas no MySQL**:  
   Siga as instruções detalhadas no arquivo [tabelas.md](tabelas.md) para criar as tabelas no seu banco de dados MySQL.


3. **Gerar e Inserir Dados**:
   Execute o script `gerar_dados.py` para gerar dados fictícios e populá-los no banco:
   ```bash
   python gerar_dados.py
   ```

4. **Rodar o Pipeline ETL**:
   Execute o script principal para realizar o ETL e exportar o arquivo CSV:
   ```bash
   python main.py
   ```

---

### **Estruturas do Banco de Dados**
Veja os detalhes no arquivo [create_tables.md](scripts/create_tables.md) para as instruções completas de criação das tabelas.

---

### **Requisitos**
- Python 3.11 ou superior
- MySQL 8.0 ou superior
- Dependências listadas em `requirements.txt`