from flask import Flask
from databaser import Database

app = Flask(__name__)
db = Database(__name__)
err = 0;

@app.route('/')
def test_site():
    return 'Тестовый сайт'

@app.errorhandler(404)
def page_not_found(e):
    db.add_id(str(err))
    err += 1
    return f'Страница не существует или она удалена, кол-во ошибок в Database: {err}', 404
