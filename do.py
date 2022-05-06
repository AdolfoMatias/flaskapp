from flask import render_template, request,Flask

import os

app = Flask(__name__)




@app.route("/")
@app.route("/index/")
def novo():
    
    dados = {"profissao": "Profissao"}
    
    return render_template("index.html",  dados=dados)
   

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login")
def login():
    return render_template("login.html")

# @app.route("/autenticar", methods=["GET"])
# def autenticar():
#     usuar= request.args.get("usuar")
#     passo= request.args.get("passo")
#     return f"{str(usuar)}, {str(passo)}"

@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuar= request.form.get("usuar")
    passo= request.form.get("passo")
    return f"{str(usuar)}, {str(passo)}"




    
# def  add():
#     a=request.form["a"]
#     b=request.form["b"]

#     return str(int(a)+int(b))


if __name__=="__main__":
    port = int(os.getenv("PORT", '5000'))
    

    app.run(host="0.0.0.0", port=port)
    #colocar no .flaskenv
    #FLASK_ENV=development(modo de produção)






