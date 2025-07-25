import csv
from models import db, Ayat
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosbane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CSV_PATH = 'quran.csv'

def seed_ayat():
    with app.app_context():
        with open(CSV_PATH, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                try:
                    sura = int(row['surah'])
                    num_aya = int(row['ayah'])
                except (ValueError, KeyError):
                    continue
                text = row.get('text', '')
                ayat = Ayat(sura=sura, num_aya=num_aya, text=text)
                db.session.add(ayat)
                count += 1
            db.session.commit()
            print(f"Seeded {count} ayat from {CSV_PATH}.")

if __name__ == "__main__":
    seed_ayat()
