import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        database='veiculos'
    )
    return conexao

def inserir_veiculos():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    id_modelo = int(input('Qual o id do modelo? '))
    ano = int(input('Qual o ano do modelo? '))
    placa = input('Qual a placa do veiculo? ')
    id_categoria = int(input('Qual o id da categoria? '))
    sql = 'INSERT INTO veiculos (id_modelo, ano, placa, id_categoria) VALUES (%s, %s, %s, %s)'
    val = (id_modelo, ano, placa, id_categoria)
    meu_cursor.execute(sql, val)
    conexao.commit()
    print(meu_cursor.rowcount, 'record inserted.')
    meu_cursor.close()
    conexao.close()

def inserir_modelos():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    nome = input('Qual o nome do modelo? ')
    sql = 'INSERT INTO modelos (nome) VALUES (%s)'
    val = (nome,)
    meu_cursor.execute(sql, val)
    conexao.commit()
    print(meu_cursor.rowcount, 'record inserted.')
    meu_cursor.close()
    conexao.close()

def inserir_categorias():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    nome = input('Qual o nome da categoria?')
    sql = 'INSERT INTO categorias (nome) VALUES (%s)'
    val = (nome,)
    meu_cursor.execute(sql, val)
    conexao.commit()
    print(meu_cursor.rowcount, 'record inserted.')
    meu_cursor.close()
    conexao.close()

def listar_veiculos():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    sql = 'SELECT v.id, v.id_modelo,  m.nome AS nome_modelo, v.ano, v.placa FROM veiculos v JOIN modelos m ON v.id_modelo = v.id'
    meu_cursor.execute(sql)
    linhas = meu_cursor.fetchall()
    print(f'{"id":^12}{"id_modelo":^10}{"nome_modelo":^14}{"ano":^0}{"placa":^0}')
    for id, id_modelo, nome, ano, placa in linhas:
        print(id,'\t', id_modelo,'\t', nome,'\t', ano, '\t', placa)
    meu_cursor.close()
    conexao.close()

def listar_modelos():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    meu_cursor.execute('SELECT * FROM modelos')
    linhas = meu_cursor.fetchall()
    print(f'{"id":<9}{"nome":>0}')
    for id, nome, in linhas:
        print(id,'\t', nome)
    meu_cursor.close()
    conexao.close()

def listar_categorias():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    meu_cursor.execute('SELECT * FROM categorias')
    categorias = meu_cursor.fetchall()
    print(f'{"id":^10}{"Nome":^0}')
    for id, nome in categorias:
        print(id,'\t',nome)
    meu_cursor.close()
    conexao.close()

def alterar():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    id = int(input('Qual id você quer alterar? '))
    ano = input('Qual o novo ano do veiculo? ')
    sql = 'UPDATE veiculos SET ano = %s where id = %s'
    val = (ano, id)
    meu_cursor.execute(sql, val)
    conexao.commit()
    print(meu_cursor.rowcount, 'record inserted.')
    meu_cursor.close()
    conexao.close()

def deletar():
    conexao = conectar()
    listarveiculos()
    meu_cursor = conexao.cursor()
    deletar = int(input('Qual id você quer apagar? '))
    sql = 'DELETE FROM veiculos WHERE id = %s'
    val = (deletar,)
    meu_cursor.execute(sql, val)
    conexao.commit()
    print(meu_cursor.rowcount, 'record inserted.')
    meu_cursor.close()
    conexao.close()

def pesquisar():
    conexao = conectar()
    meu_cursor = conexao.cursor()
    pesquisar = input('Qual o nome do modelo deseja pesquisar? ')
    sql = 'SELECT * FROM modelos WHERE nome = %s'
    val = (pesquisar,)
    meu_cursor.execute(sql, val)
    modelos = meu_cursor.fetchall()
    for id, nome, in modelos:
        print(id, nome)
    meu_cursor.close()
    conexao.close()

while True:
    print('1.Inserir Veiculos')
    print('2.Inserir Modelos')
    print('3.Inserir Categorias')
    print('4.Listar Veiculos')
    print('5.Listar Modelos')
    print('6.Listar Categorias')
    print('7.Alterar')
    print('8.Deletar')
    print('9.Pesquisar')
    print('10.Sair')
    opcao = int(input('Qual das opções você deseja? '))
    if opcao == 1:
        inserir_veiculos()
    elif opcao == 2:
        inserir_modelos()
    elif opcao == 3:
        inserir_categorias()
    elif opcao == 4:
        listar_veiculos()
    elif opcao == 5:
        listar_modelos()
    elif opcao == 6:
        listar_categorias()
    elif opcao == 7:
        alterar()
    elif opcao == 8:
        deletar()
    elif opcao == 9:
        pesquisar()
    else: 
        print('Sair')
        break 