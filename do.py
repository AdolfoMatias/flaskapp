from app import app
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
    app.run(port=7000)





