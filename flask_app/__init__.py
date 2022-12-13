from flask import Flask
app = Flask(__name__)
app.secret_key = "Ninjas don't lie!"
DATABASE = "login_and_register_schema"