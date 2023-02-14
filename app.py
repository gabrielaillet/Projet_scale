import flask
from database.models import *
import datetime
now = datetime.datetime.now()
one_hour_ago = now - datetime.timedelta(0, hours=1)


app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Yves\\Desktop\\WEB\\Projet_scale\\database\\database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"


db.init_app(app)

with app.test_request_context():
    db.create_all()


# @app.route("/clean")
def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"



if __name__ == '__main__':
    app.run(debug=True)
