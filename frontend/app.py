from flask import Flask, render_template
from flasgger import Swagger
from api import api_bp

app = Flask(__name__)
swagger = Swagger(app)
app.register_blueprint(api_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
