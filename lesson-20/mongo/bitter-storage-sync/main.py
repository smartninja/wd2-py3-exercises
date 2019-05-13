from flask import Flask
from handlers.bitts import bitt_handlers

app = Flask(__name__)
app.register_blueprint(bitt_handlers)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="5000")
