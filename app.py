from flask import Flask, render_template , request , redirect;

app = Flask(__name__)

@app.route("/")
def login():
    return render_template ("login.html")


@app.route("/painel")
def painel():
    return render_template ("painel.html")

@app.route("/verificar" , methods=['POST'])
def verificar():
    CPF = request.form.get('CPF')
     senha = request.form.get('senha')

print('Tentando login com:', CPF,'/SENHA',senha)

  return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)
