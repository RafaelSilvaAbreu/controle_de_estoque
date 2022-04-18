from flask import Flask, render_template, request
from banco import inserte_dados, estoque, delatarEstoque, saida_de_estoque, registrar_usuario, registro_de_usuarios, pesquisa_prod, entrada_prod, dados_relatorio, relatorio_ent_sai
from datetime import datetime

usu = "Usuário"

app = Flask(__name__)

#abrir paginas
@app.route('/')
def abre_index():
    return render_template('login.html', usuario_a1 = usu)

@app.route('/login')
def abre_login():
    return render_template('login.html', usuario_a1 = usu)

@app.route('/registrar')
def abre_registro():
    return render_template('registrar.html', usuario_a1 = usu)

@app.route('/index')
def abre_home():
    return render_template('index.html', usuario_a1 = usu )

@app.route('/Insere_itens')
def abre_insere():
    return render_template('Insere_itens.html', usuario_a1 = usu)

@app.route('/Estoque')
def abre_estoque():
    lista = estoque()
    return render_template('Estoque.html', listar = lista, usuario_a1 = usu)

#---------------------------------------------------------------------------------------
#Registrar na aplicação do sistema

@app.route('/registrar_user', methods=['POST'])
def registrar_usuAplicacao():
    user_login_registrado = request.form['nome_login_registrar']
    user_senha_registrado = request.form['senha_login_registrar']
    registrar_usuario(user_login_registrado, user_senha_registrado)
    return render_template('login.html')


#Logar na aplicação do sistema
@app.route('/logar_user', methods=['POST'])
def logar_aplicacao():
    user_login = request.form['nome_login']
    user_senha = request.form['senha_login']
    verifica = registro_de_usuarios(user_login, user_senha)
    usu = user_login
    if verifica > 0:
        return render_template('/index.html', usuario_a1 = usu)
    else:
        return render_template('login.html', mensagem = 'usuário ou senha inválido!')


#----------------------------------------------------------------------------------------
#insirir dados no banco de dados

@app.route('/Insere_itens', methods=['POST'])
def registrar_produtos():
    nomeP = request.form['nome_produto']
    valorP = request.form['valor_produto']
    quantidadeP = request.form['quantidade_produto']
    unidadeP = request.form['unidade_de_medida']
    data_de_entrada = datetime.now()
    inserte_dados(nomeP, valorP, quantidadeP, unidadeP, data_de_entrada)
    return render_template('Insere_itens.html')



@app.template_filter()
def formata_moeda(valor):
    valor = float(valor) 
    return 'R${:,.2f}'.format(valor)



@app.route('/excluir_item', methods = ['POST'])
def excluirs_item():
    nome_excluido = request.form['idProd']
    delatarEstoque(nome_excluido)
    lista = estoque()
    return render_template('Estoque.html', listar = lista)




@app.route('/saida')
def abre_pagina_saida():
    return render_template('saida.html', usuario_a1 = usu)

@app.route('/saida', methods=['POST'])
def atualizar_produtos():
    nome_atu = request.form['atualiar_pro']
    quantidade_atu = request.form['atualizar_prod_quan']
    lista = pesquisa_prod(nome_atu)
    for l in lista:
        if int(quantidade_atu) > l[3]: 
            return render_template('saida.html', listar = lista, mensagem='valor acima do que tem em estoque!!')
        else:
            saida_de_estoque(nome_atu, quantidade_atu)
            dataSaida = datetime.now()
            nome_funcao = 'Saída'
            dados_relatorio(nome_funcao, nome_atu, quantidade_atu, dataSaida)
            return render_template('saida.html', listar = lista, msg = 'saida de produto com sucesso!!')

#----------------------------------------------------------------------------------

@app.route('/entrada')
def abre_pag_entrada():
    return render_template('entrada.html', usuario_a1 = usu)


@app.route('/entrada', methods=['POST'])
def pag_entrada():
    nome_a = request.form['entrar_pro']
    quantidade_a = request.form['entrar_prod_quan']
    entrada_prod(nome_a, quantidade_a)
    dataEntrada = datetime.now()
    nome_funcao = 'Entrada'
    dados_relatorio(nome_funcao, nome_a, quantidade_a, dataEntrada)
    return render_template('entrada.html', msg = 'Produto entrou com sucesso!!')



@app.route('/relatorios')
def abre_relatorio():
    rel =  relatorio_ent_sai()
    return render_template('relatorios.html', listar = rel, usuario_a1 = usu)

#debug=True serve para atualizar sem reiniciar o servidor
if __name__=="__main__":
    app.run(debug=True)