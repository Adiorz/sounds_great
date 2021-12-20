import os
import random

from flask import Flask, jsonify, send_from_directory, render_template
from glob import glob
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from loguru import logger as log

sounds = []
for file in glob('sounds/*'):
    mp3 = file.split("\\")[-1]
    try:
        attrs = dict(EasyID3(file))
        attrs['length'] = MP3(file).info.length
        attrs['url'] = file
        sounds.append(attrs)
    except():
        pass

CATEGORIES = """Mityczne stworzenia
Rośliny
Części ciała
Kolory
Gry planszowe
Bogowie
Aktorzy
Marki samochodów
Rzeki
Zawody
Państwa
Potrawy
Meble
Zjawiska pogodowe
Liczby
Dania
Bajki
Owoce
Warzywa
Kwiaty
Języki
Części garderoby"""


app = Flask(__name__)


def get_sorted_sounds():
    return sorted(sounds, key=lambda s: int(s['url'].split("sounds\\")[1].split('.')[0]))


@app.route('/sounds/<path:path>')
def send_file(path):
    return send_from_directory('sounds', path)


@app.route('/index')
def index():
    return jsonify(sounds)


@app.route('/', methods=['GET'])
def play():  # pragma: no cover
    return render_template("index.html", sounds=sounds, category=random.choice(CATEGORIES.lower().split('\n')))


if __name__ == "__main__":
    app.run(debug=True)
