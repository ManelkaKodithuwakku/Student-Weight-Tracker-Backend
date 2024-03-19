from flask import Flask

from controller.controller import Controller


class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        Controller(self.app)

if __name__ == '__main__':
    flask_app = FlaskApp()
    flask_app.app.run(debug=True, host="127.0.0.1", port=3000)