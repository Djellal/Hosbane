import csv
from flask import Flask
from models import db, Ayat

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosbane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CSV_PATH = 'quran.csv'

def seed_ayat():
    with app.app_context():
        with open(CSV_PATH, encoding='utf-8') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if len(row) != 3:
                    continue
                try:
                    sura = int(row[0])
                    num_aya = int(row[1])
                    text = row[2]
                except ValueError:
                    continue
                ayat = Ayat(sura=sura, num_aya=num_aya, text=text)
                db.session.add(ayat)
                count += 1
            db.session.commit()
            print(f"Seeded {count} ayat from {CSV_PATH}.")

if __name__ == "__main__":
    seed_ayat()
