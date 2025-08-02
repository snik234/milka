﻿""" Програма використовує flask та запускає веб-сервер.
При запиті на цей сервер він повертає вміст файлу index.html
У цій версії передбачається, що файл може бути шаблон.
 """
from flask import Flask, render_template
import os
def index():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('index.html')

def art():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('art.html')
def food():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('food.html')
    
def history():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('history.html')
    
def food():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('food.html')

def traditions():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('traditions.html')

def attractions():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('attractions.html')

folder = os.getcwd() # запам'ятали поточну робочу папку
# Створюємо об'єкт веб-додатку:
app = Flask(__name__, template_folder=folder, static_folder=folder)
#перший параметр - ім'я модуля
# параметр з ім'ям static_folder визначає ім'я папки, що містить статичні файли
# параметр з ім'ям template_folder визначає ім'я папки, що містить шаблони


# створюємо правило дляURL '/':
app.add_url_rule('/', 'index', index)
app.add_url_rule('/history.html', 'history', history)
app.add_url_rule('/art.html', 'art', art)
app.add_url_rule('/food.html', 'food', food)
app.add_url_rule('/attractions.html', 'attractions', attractions)
app.add_url_rule('/traditions.html', 'traditions', traditions)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
