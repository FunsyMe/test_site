from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_site():
    return 'Тестовый сайт'

@app.errorhandler(404)
def page_not_found(e):
    return 'Страница не существует или она удалена', 404

if __name__ == '__main__':
    app.run(debug=True)
