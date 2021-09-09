import mysql.connector


def criarDatabase(nome_database):   
    banco = mysql.connector.connect(host='localhost',
                                user='root', 
                                password='',)
    cursor = banco.cursor()      
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_database};")
    banco.commit()
    print(f'Database {nome_database} foi criado com sucesso')

def criartable(nome_database, nome_table):
    banco = mysql.connector.connect(host='localhost',
                                        user='root', 
                                        password='',
                                        database=nome_database)

    table = (f"CREATE TABLE IF NOT EXISTS `{nome_table}` ("
        "  `ID` INT NOT NULL AUTO_INCREMENT,"
        "  `Codigo` INT,"
        "  `Nome` VARCHAR(50),"
        "  `Preço` DOUBLE,"
        "  `Categoria` VARCHAR(50),"
        "  PRIMARY KEY (`ID`)"
        ") ENGINE=InnoDB")
    cursor = banco.cursor()      
    cursor.execute(table)
    banco.commit()
    print(f'Tabela {nome_table} foi criado com sucesso')

def conectar_base():
    banco = mysql.connector.connect(host='localhost',
                                        user='root', 
                                        password='',
                                        database='cadastrodeprodutos')
    return banco
    
def inseridados(codigo=None, nome=None, preco=None, categoria=None):
    banco = mysql.connector.connect(host='localhost',
                                        user='root', 
                                        password='',
                                        database='cadastrodeprodutos')
    add_produtos = ("INSERT INTO produtos "
                "(Codigo, Nome, Preço, Categoria) "
                "VALUES (%s, %s, %s, %s)")
    dados_produtos = (str(codigo), str(nome), str(preco), categoria)                                    
    cursor = banco.cursor()      
    cursor.execute(add_produtos, dados_produtos)
    banco.commit()
    print('Os Dados foram inseridos com sucesso')

def visualizarDados():
    banco = mysql.connector.connect(host='localhost',
                                        user='root', 
                                        password='',
                                        database='cadastrodeprodutos')
    cursor = banco.cursor()      
    cursor.execute("SELECT * FROM produtos;")
    dados_lidos = cursor.fetchall()
    return dados_lidos
