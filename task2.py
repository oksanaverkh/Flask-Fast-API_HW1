# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_task2_about.html')


@app.route('/clothes/')
def clothes():
    return render_template('index_task2_clothes.html')


@app.route('/shoes/')
def shoes():
    return render_template('index_task2_shoes.html')

@app.route('/dresses/')
def dresses():
    return render_template('index_task2_dresses.html')

if __name__ == "__main__":
    app.run(debug=True)