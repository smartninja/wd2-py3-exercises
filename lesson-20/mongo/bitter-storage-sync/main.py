from flask import Flask
from handlers.bitts import bitt_handlers
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(bitt_handlers)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="5000")
