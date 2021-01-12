# Import thư viện chuẩn

# Import thư viện bên ngoài
from flask import Flask, render_template

# Import module, package trong project
from boitoan.route import boi

app = Flask(__name__, template_folder="template")

# Register blueprint
app.register_blueprint(boi)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # アプリ開始
    app.run(host="127.0.0.1", port=5000, debug=True)



