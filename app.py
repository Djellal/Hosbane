

# ...existing code...

from flask import Flask, render_template


from flask_migrate import Migrate
from models import db, Sura, Ayat


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosbane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Inject sura_list into all templates
@app.context_processor
def inject_sura_list():
    try:
        sura_list = Sura.query.order_by(Sura.num_sura).all()
    except Exception:
        sura_list = []
    return dict(sura_list=sura_list)


@app.route('/')
def home():
    return render_template('home.html')

from flask import request

@app.route('/sura')
def sura_nav():
    num_sura = request.args.get('num_sura', type=int)
    sura = Sura.query.get(num_sura) if num_sura else None
    ayat = Ayat.query.filter_by(sura=num_sura).order_by(Ayat.num_aya).all() if num_sura else []
    return render_template('sura.html', sura=sura, ayat=ayat)

@app.route('/verses')
def verses_nav():
    # Placeholder: implement verses range navigation logic
    return '<h2>صفحة الآيات (تحت الإنشاء)</h2>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
