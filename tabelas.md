## Criação banco de dados

```
CREATE DATABASE teste;
USE teste;
```
## Tabelas
### Associado
```
CREATE TABLE associado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) NOT NULL
);

```

### Conta
```
CREATE TABLE conta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50) NOT NULL,
    data_criacao TIMESTAMP NOT NULL,
    id_associado INT NOT NULL,
    FOREIGN KEY (id_associado) REFERENCES associado(id)
);
```

### Cartão
```
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

### Movimento
```
CREATE TABLE movimento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vlr_transacao DECIMAL(10, 2) NOT NULL,
    des_transacao VARCHAR(255) NOT NULL,
    data_movimento TIMESTAMP NOT NULL,
    id_cartao INT NOT NULL,
    FOREIGN KEY (id_cartao) REFERENCES cartao(id)
);
```