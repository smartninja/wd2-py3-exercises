from flask import Flask
from handlers.auth import auth_handlers
from handlers.topic import topic_handlers

app = Flask(__name__)
app.register_blueprint(auth_handlers)
app.register_blueprint(topic_handlers)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="5001")
