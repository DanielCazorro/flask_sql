from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()  # Configura la aplicación utilizando variables de entorno con prefijo.
