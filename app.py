from flask import Flask, render_template
from flask import Blueprint

app = Flask(__name__, static_folder='static', template_folder='templates')

# Данные для хлебных крошек
PAGE_NAMES = {
    'home': 'Рабочий стол',
    'zoom': 'Zoom',
    'games': 'Игры',
    'news': 'Новости',
    'youtube': 'YouTube',
    'delivery': 'Доставка',
    'music': 'Музыка',
    'gallery': 'Галерея',
    'game_amongus': 'Among Us',
    'game_tlou2': 'The Last of Us Part II',
    'game_cyberpunk': 'Cyberpunk 2077',
    'game_animalcrossing': 'Animal Crossing: New Horizons',
    'game_phasmo': 'Phasmophobia',
    'game_fallguys': 'Fall Guys',
}

# Данные для навигации
NAV_ITEMS = [
    {'id': 'home', 'name': 'Главная'},
    {'id': 'zoom', 'name': 'Zoom'},
    {'id': 'games', 'name': 'Игры'},
    {'id': 'news', 'name': 'Новости'},
    {'id': 'youtube', 'name': 'YouTube'},
    {'id': 'delivery', 'name': 'Доставка'},
    {'id': 'music', 'name': 'Музыка'},
    {'id': 'gallery', 'name': 'Галерея'}
]

views = Blueprint('views', __name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                         page_id='home',
                         page_name=PAGE_NAMES['home'],
                         nav_items=NAV_ITEMS)


@app.route('/zoom')
def zoom():
    return render_template('zoom.html',
                         page_id='zoom',
                         page_name=PAGE_NAMES['zoom'],
                         nav_items=NAV_ITEMS)


@app.route('/games')
def games():
    return render_template('games.html',
                         page_id='games',
                         page_name=PAGE_NAMES['games'],
                         nav_items=NAV_ITEMS)


@app.route('/games/phasmophobia')
def game_phasmo():
    return render_template('game_phasmo.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_phasmo']}",
                         nav_items=NAV_ITEMS)


@app.route('/games/fallguys')
def game_fallguys():
    return render_template('game_fallguys.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_fallguys']}",
                         nav_items=NAV_ITEMS)


@app.route('/games/amongus')
def game_amongus():
    return render_template('game_amongus.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_amongus']}",
                         nav_items=NAV_ITEMS)

@app.route('/games/the-last-of-us-2')
def game_tlou2():
    return render_template('game_tlou2.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_tlou2']}",
                         nav_items=NAV_ITEMS)


@app.route('/games/cyberpunk2077')
def game_cyberpunk():
    return render_template('game_cyberpunk.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_cyberpunk']}",
                         nav_items=NAV_ITEMS)


@app.route('/games/animal-crossing')
def game_animalcrossing():
    return render_template('game_animalcrossing.html',
                         page_id='games',
                         page_name=f"Игры » {PAGE_NAMES['game_animalcrossing']}",
                         nav_items=NAV_ITEMS)


@app.route('/news')
def news():
    return render_template('news.html',
                         page_id='news',
                         page_name=PAGE_NAMES['news'],
                         nav_items=NAV_ITEMS)


@app.route('/delivery')
def delivery():
    return render_template('delivery.html',
                         page_id='delivery',
                         page_name=PAGE_NAMES['delivery'],
                         nav_items=NAV_ITEMS)


@app.route('/music')
def music():
    return render_template('music.html',
                         page_id='music',
                         page_name=PAGE_NAMES['music'],
                         nav_items=NAV_ITEMS)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html',
                         page_id='gallery',
                         page_name=PAGE_NAMES['gallery'],
                         nav_items=NAV_ITEMS)


@app.route('/youtube')
def youtube():
    return render_template('youtube.html',
                         page_id='youtube',
                         page_name=PAGE_NAMES['youtube'],
                         nav_items=NAV_ITEMS)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
