from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET","POST"])
def home():
    if (request.method =="GET"):
        return render_template("index.html")
    else:
         if(request.form["n1"] != "" and request.form ["n2"] != ""):
           mult= int(request.form["n1"]) * int(request.form["n2"])
           return str(mult)
         else:
            return "Informe um Numero Válido"

@app.route("/result")
def result(n1,n2):
   return render_template("result.html")

@app.errorhandler(404)
def not_foud(error):
    return render_template("error.html")

app.run(port=5000, debug=True)