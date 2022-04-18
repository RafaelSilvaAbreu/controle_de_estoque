import cmd
from click import command
import mysql.connector as mc


banco = mc.connect(host='localhost', user='root', password='admin',database='bd_estoque')






#registrar usuario ------------------------------------------------------------------------------------

def registrar_usuario(loginU, senhaU):
    if banco.is_connected():
        comando = 'insert into login_usuario (nome, senha) values (%s, %s)'
        cursor = banco.cursor()
        valores = (loginU, senhaU)
        cursor.execute(comando, valores)
        banco.commit()
        return 'Usuario registrado com sucesso!'
    else:
        return 'Erro ao salvar dados!'


#logar usuario 

def registro_de_usuarios(loginUSU, senhaUSU):
     if banco.is_connected():
        consulta = "select nome, senha from login_usuario where nome = %s and senha = %s"
        valores = (loginUSU, senhaUSU)
        cursor = banco.cursor()
        cursor.execute(consulta, valores)

        return len(cursor.fetchall())

#------------------------------------------------------------------------------------------




#insirir dados no banco de dados -------------------------------------------------------------------------------
def inserte_dados(nomeM, valorM, qntM, uniM, dataM):
    if banco.is_connected():
        comando = 'insert into mercadorias (nome_produto, valor_produto, quantidade_produto, unidade_medida, data_entrada) values (%s, %s, %s, %s, %s)'
        cursor = banco.cursor()
        valores = (nomeM, valorM, qntM, uniM, dataM)
        cursor.execute(comando, valores)
        banco.commit()
        return 'Salvo com sucesso!!'
    else:
        return 'Erro ao salvar!!!'


def estoque():
    if banco.is_connected():
        cursor = banco.cursor()
        cmdSelect = 'select * from mercadorias'
        cursor.execute(cmdSelect)
        return cursor.fetchall()


def delatarEstoque(id_excluido):
    if banco.is_connected():
        cursor = banco.cursor()
        sql = 'delete from mercadorias where id_mercadoria = %s'
        valor = (id_excluido,)
        cursor.execute(sql, valor)
        banco.commit()


def saida_de_estoque(nome_Pro, qntPro):
    if banco.is_connected():
        cursor = banco.cursor()
        nomePro = (f'%{nome_Pro}%')
        sql = 'update mercadorias set quantidade_produto = quantidade_produto - %s where nome_produto like %s'
        valor = (qntPro, nomePro)
        cursor.execute(sql, valor)
        banco.commit()
#-------------------------------------------------------------------------------------------------------

def pesquisa_prod(nomeP):
    if banco.is_connected():
        cursor = banco.cursor()
        nome_produto = (f'%{nomeP}%')
        cmdDeProcura = 'select * from mercadorias where nome_produto like %s'
        nomeProduto = (nome_produto,)
        cursor.execute(cmdDeProcura, nomeProduto)
        valor = cursor.fetchall()
        return valor


def entrada_prod(nome_prod, qnt_prod):
    if banco.is_connected():
        cursor = banco.cursor()
        nomeP = (f'%{nome_prod}%')
        cmdEntrada = 'update mercadorias set quantidade_produto = quantidade_produto + %s where nome_produto like %s'
        valores = (qnt_prod, nomeP)
        cursor.execute(cmdEntrada, valores)
        banco.commit()


def dados_relatorio(nome_fuc, nomeP, qnt, data):
    if banco.is_connected():
        comando = 'insert into relatorio (nome_f, nome_prod, qnt, dataRel) values (%s, %s, %s, %s)'
        cursor = banco.cursor()
        valores = (nome_fuc, nomeP, qnt, data)
        cursor.execute(comando, valores)
        banco.commit()
       


def relatorio_ent_sai():
    if banco.is_connected():
        cursor = banco.cursor()
        comandoSql = 'select * from relatorio'
        cursor.execute(comandoSql)
        return cursor.fetchall()

