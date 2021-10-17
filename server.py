from flask import Flask, jsonify, send_from_directory, render_template
from glob import glob
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from loguru import logger as log

log.info('hi')

SOUNDS = {
    "0.empty.mp3": "https://drive.google.com/uc?export=download&id=1_lOAzrjZR7QdOf1HmMFyI5at9z-6JGr9",
    "1.krowa.mp3": "https://drive.google.com/uc?export=download&id=1b0rcc_ibCIAV3bjJCs6KANs8iEXVm-Xe",
    "2.klawiatura.mp3": "https://drive.google.com/uc?export=download&id=1X1lpIbjl1t4E4dhidd-z1Qcp8C48zf9f",
    "3.szklo.mp3": "https://drive.google.com/uc?export=download&id=1w-ACdjSjeZmvsRSxg05WVe4Mx2MIGC5f",
    "4.wybuch.mp3": "https://drive.google.com/uc?export=download&id=1-uGrINo5YNMuIKagB5vD2SbBFYB9Zd9x",
    "5.klakson.mp3": "https://drive.google.com/uc?export=download&id=1HM0xo0eFLy0nAh9tpxSm-MnAiVaGHKyR",
    "6.kon.mp3": "https://drive.google.com/uc?export=download&id=1PGHZZluZTzEyxVvuauDN5j235NoL204-",
    "7.woda.mp3": "https://drive.google.com/uc?export=download&id=1NxFFrC8Zu2uUapw_bw3p3PyQeGatOeNB",
    "8.wiatr.mp3": "https://drive.google.com/uc?export=download&id=140L66jlXjKwRpj9jR-Q1EE70tE8IM1Bo",
    "9.zamek.mp3": "https://drive.google.com/uc?export=download&id=1g5jNn4KItiDbb5byAWvkPWZ8iSA6P1oc",
    "10.zegar.mp3": "https://drive.google.com/uc?export=download&id=1BTxH2K_94GIlc3wl_QI36GZuGQKPh17m",
    "11.fajerwerki.mp3": "https://drive.google.com/uc?export=download&id=1o6Fq1m0T21U_eOxWEPvMNpc5KnjT6Dh-",
    "12.liscie.mp3": "https://drive.google.com/uc?export=download&id=1ityTpoXbJlxCjfSSaiuSbWnPctIbb406",
}

sounds = []
for file in glob('sounds/*'):
    mp3 = file.split("\\")[-1]
    try:
        attrs = dict(EasyID3(file))
        attrs['length'] = MP3(file).info.length
        # attrs['url'] = SOUNDS[mp3]
        attrs['url'] = file
        sounds.append(attrs)
    except():
        pass

app = Flask(__name__)


@app.route('/sounds/<path:path>')
def send_file(path):
    return send_from_directory('sounds', path)


@app.route('/index')
def index():
    return jsonify(sounds)


@app.route('/', methods=['GET'])
def play():  # pragma: no cover
    return render_template("index.html", sounds=sounds)


if __name__ == "__main__":
    app.run()
