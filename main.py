from pyspark.sql import SparkSession
import pandas as pd
import os

# Configurar Spark
spark = SparkSession.builder \
    .appName("ETL MySQL to CSV") \
    .config("spark.jars", "mysql-connector-j-9.1.0.jar") \
    .config("spark.hadoop.io.nativeio.nativepath", "false") \
    .getOrCreate()

# Configurar conexão com MySQL
mysql_url = "jdbc:mysql://localhost:3306/teste"
mysql_properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Ler tabelas do MySQL
associado = spark.read.jdbc(url=mysql_url, table="associado", properties=mysql_properties)
conta = spark.read.jdbc(url=mysql_url, table="conta", properties=mysql_properties)
cartao = spark.read.jdbc(url=mysql_url, table="cartao", properties=mysql_properties)
movimento = spark.read.jdbc(url=mysql_url, table="movimento", properties=mysql_properties)

# Realizar os joins para criar a visão única
df_movimento_flat = movimento \
    .join(cartao, movimento.id_cartao == cartao.id) \
    .join(conta, cartao.id_conta == conta.id) \
    .join(associado, conta.id_associado == associado.id) \
    .select(
        associado.nome.alias("nome_associado"),
        associado.sobrenome.alias("sobrenome_associado"),
        associado.idade.alias("idade_associado"),
        associado.email.alias("email_associado"),
        movimento.vlr_transacao.alias("vlr_transacao_movimento"),
        movimento.des_transacao.alias("des_transacao_movimento"),
        movimento.data_movimento.alias("data_movimento"),
        cartao.nom_impresso.alias("nome_impresso_cartao"),
        conta.tipo.alias("tipo_conta"),
        conta.data_criacao.alias("data_criacao_conta")
    )

# Mostrar resultado no console (opcional)
df_movimento_flat.show()

movimento_flat_pandas = df_movimento_flat.toPandas()


# Verifica se o diretório 'output' existe
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Cria o diretório se ele não existir

# Salvar resultado como CSV
movimento_flat_pandas.to_csv("output/movimento_flat.csv", index=False, sep=";", encoding="utf-8")
# movimento_flat_pandas.to_csv("C:/temp/movimento_flat.csv", index=False, sep=";", encoding="utf-8")
