import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root", 
            database="teste"
        )
        if conexao.is_connected():
            print("Conexão ao MySQL bem-sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para gerar e inserir os dados
def gerar_dados(conexao):
    try:
        fake = Faker('pt_BR')
        cursor = conexao.cursor()

        # Inserir dados na tabela `associado`
        sql_associado = """
        INSERT INTO associado (nome, sobrenome, idade, email)
        VALUES (%s, %s, %s, %s)
        """
        dados_associado = []

        for _ in range(10):  # Gerar 10 associados
            nome = fake.first_name()
            sobrenome = fake.last_name()
            email = f"{nome.lower()}.{sobrenome.lower()}@example.com"
            idade = random.randint(18, 80)
            dados_associado.append((nome, sobrenome, idade, email))

        cursor.executemany(sql_associado, dados_associado)

        # Recuperar IDs dos associados
        cursor.execute("SELECT id, nome, sobrenome FROM associado")
        associados = cursor.fetchall()  # [(id, nome, sobrenome), ...]

        # Inserir dados na tabela `conta`
        sql_conta = """
        INSERT INTO conta (tipo, data_criacao, id_associado)
        VALUES (%s, %s, %s)
        """
        tipos_conta = ['Corrente', 'Poupança']
        dados_conta = []

        for associado in associados:
            num_contas = random.randint(1, 3)  # Cada associado pode ter entre 1 e 3 contas
            for _ in range(num_contas):
                dados_conta.append(
                    (random.choice(tipos_conta), fake.date_time_this_year(), associado[0])
                )
        cursor.executemany(sql_conta, dados_conta)

        # Recuperar IDs das contas
        cursor.execute("SELECT id, id_associado FROM conta")
        contas = cursor.fetchall()  # [(id_conta, id_associado), ...]

        # Inserir dados na tabela `cartao`
        sql_cartao = """
        INSERT INTO cartao (num_cartao, nom_impresso, id_conta, id_associado)
        VALUES (%s, %s, %s, %s)
        """
        dados_cartao = []

        for conta in contas:
            associado_id = conta[1]
            # Recuperar o nome completo do associado correspondente
            associado = next(a for a in associados if a[0] == associado_id)
            nome_completo = f"{associado[1]} {associado[2]}"
            dados_cartao.append(
                (fake.credit_card_number(), nome_completo, conta[0], associado_id)
            )
        cursor.executemany(sql_cartao, dados_cartao)

        # Recuperar IDs dos cartões
        cursor.execute("SELECT id, id_conta FROM cartao")
        cartoes = cursor.fetchall()  # [(id_cartao, id_conta), ...]

        # Inserir dados na tabela `movimento`
        sql_movimento = """
        INSERT INTO movimento (vlr_transacao, des_transacao, data_movimento, id_cartao)
        VALUES (%s, %s, %s, %s)
        """
        descricoes = ['Compra em supermercado', 'Restaurante', 'Pagamento de contas', 'Saques']
        dados_movimento = []

        for cartao in cartoes:
            for _ in range(10):  # 10 movimentos por cartão
                dados_movimento.append(
                    (round(random.uniform(10, 1000), 2),
                     random.choice(descricoes),
                     fake.date_time_this_year(),
                     cartao[0])
                )
        cursor.executemany(sql_movimento, dados_movimento)

        # Confirmar transações
        conexao.commit()
        print("Dados gerados e inseridos com sucesso!")

    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        conexao.rollback()

# Executar o programa
if __name__ == "__main__":
    conexao = conectar()
    if conexao:
        gerar_dados(conexao)
        conexao.close()
