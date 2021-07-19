from flask import Flask
from controllers import app_blueprint

app = Flask(__name__)
app.register_blueprint(app_blueprint)
app.config['UPLOAD_EXTENSIONS'] = ['pdf']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


if __name__ == "__main__":
    app.run()