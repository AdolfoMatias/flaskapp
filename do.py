from app import app
import os

from flask import render_template


@app.route("/index")
def novo():
    nome= "Alba"
    dados = {"profissao": "Professora"}
    return render_template("index.html", dados=dados)

@app.route("/contato")
def contato():
    return render_template("contato.html")

    
# def  add():
#     a=request.form["a"]
#     b=request.form["b"]

#     return str(int(a)+int(b))


if __name__=="__main__":
    port = int(os.getenv("PORT", '5000'))

    app.run(host="0.0.0.0", port=port)
    #colocar no .flaskenv
    #FLASK_ENV=development(modo de produção)






