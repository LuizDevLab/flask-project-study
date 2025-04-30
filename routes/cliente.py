from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
 return render_template('lista_clientes.html')


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
 pass


@cliente_route.route('/new', methods=['GET'])
def form_cliente():
 """
  formulario para cadastrar um cliente
 """
 return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
 """
  exbibir detalhes do cliente
 """
 return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
 """
  formulario pra editar um cliente
 """
 return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
 """
  Atualizar detalhes do cliente
 """
 pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
 """
  delatar cliente
 """
 pass