from flask import Flask,render_template,request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/transferMoney",methods=["GET","POST"])
def transferMoney():
    return(render_template("transferMoney.html"))

@app.route("/depositMoney",methods=["GET","POST"])
def depositMoney():
    return(render_template("depositMoney.html"))

@app.route("/simpleVoting",methods=["GET","POST"])
def simpleVoting():
    return(render_template("simpleVoting.html"))


if __name__ == "__main__":
    app.run(debug=True)
