from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
  titulo = "Gestão de usuários"
  usuarios = [
    {"nome": "Luiz", "membro_ativo": True},
    {"nome": "João", "membro_ativo": False},
    {"nome": "Maria", "membro_ativo": False},
  ]
  return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
  return """
      <b>Programador python</b>: assista os videos no
      <a href="https://youtube.com/@programadorpython">Canal do youtube</a>
"""

# execucao
app.run(debug=True)