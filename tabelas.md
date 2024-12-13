# Criação do Banco de Dados e Estruturas de Tabelas

Este arquivo contém os comandos SQL necessários para criar o banco de dados e suas tabelas no MySQL. Siga os passos abaixo para configurar corretamente o banco de dados.

---

## 1. Criar o Banco de Dados

Para iniciar, crie o banco de dados `teste` e selecione-o para utilização:

```sql
CREATE DATABASE teste;
USE teste;
```

---

## 2. Criar as Tabelas

### 2.1. Tabela `associado`

A tabela `associado` armazena informações básicas sobre os associados.

```sql
CREATE TABLE associado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

- **Campos**:
  - `id`: Identificador único do associado.
  - `nome`: Nome do associado.
  - `sobrenome`: Sobrenome do associado.
  - `idade`: Idade do associado.
  - `email`: E-mail do associado.

---

### 2.2. Tabela `conta`

A tabela `conta` armazena informações das contas associadas.

```sql
CREATE TABLE conta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50) NOT NULL,
    data_criacao TIMESTAMP NOT NULL,
    id_associado INT NOT NULL,
    FOREIGN KEY (id_associado) REFERENCES associado(id)
);
```

- **Campos**:
  - `id`: Identificador único da conta.
  - `tipo`: Tipo de conta (exemplo: "corrente", "poupança").
  - `data_criacao`: Data de criação da conta.
  - `id_associado`: Referência ao associado dono da conta.

---

### 2.3. Tabela `cartao`

A tabela `cartao` armazena informações dos cartões emitidos.

```sql
CREATE TABLE cartao (
    id INT PRIMARY KEY AUTO_INCREMENT,
    num_cartao BIGINT NOT NULL,
    nom_impresso VARCHAR(100) NOT NULL,
    id_conta INT NOT NULL,
    id_associado INT NOT NULL,
    FOREIGN KEY (id_conta) REFERENCES conta(id),
    FOREIGN KEY (id_associado) REFERENCES associado(id)
);
```

- **Campos**:
  - `id`: Identificador único do cartão.
  - `num_cartao`: Número do cartão.
  - `nom_impresso`: Nome impresso no cartão.
  - `id_conta`: Referência à conta vinculada ao cartão.
  - `id_associado`: Referência ao associado dono do cartão.

---

### 2.4. Tabela `movimento`

A tabela `movimento` armazena informações das transações realizadas.

```sql
CREATE TABLE movimento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vlr_transacao DECIMAL(10, 2) NOT NULL,
    des_transacao VARCHAR(255) NOT NULL,
    data_movimento TIMESTAMP NOT NULL,
    id_cartao INT NOT NULL,
    FOREIGN KEY (id_cartao) REFERENCES cartao(id)
);
```

- **Campos**:
  - `id`: Identificador único da transação.
  - `vlr_transacao`: Valor da transação.
  - `des_transacao`: Descrição da transação.
  - `data_movimento`: Data em que a transação ocorreu.
  - `id_cartao`: Referência ao cartão utilizado na transação.

---

## Como Usar

1. **Acesse o MySQL**: Utilize seu cliente MySQL preferido para executar os comandos.

2. **Execute o Script**:
   - Copie os comandos acima e cole no terminal do MySQL, ou
   - Salve o conteúdo em um arquivo `create_tables.sql` e execute:
     ```bash
     mysql -u <usuario> -p < banco_de_dados > < create_tables.sql
     ```

3. **Valide as Estruturas**:
   Após a execução, use o comando `SHOW TABLES;` para confirmar que as tabelas foram criadas corretamente.

---

Siga as instruções acima para configurar o banco de dados e suas tabelas antes de executar o pipeline ETL.