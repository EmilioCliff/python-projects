from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint, choice

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])
def random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafe = choice(all_cafes)
    return jsonify(cafe=cafe.to_dict())

@app.route("/all", methods=['GET'])
def all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=['GET'])
def search():
    cafe_location = request.args.get("loc")
    searched_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location)).scalars().all()
    if len(searched_cafe) > 0:
        return jsonify(cafe=[cafe.to_dict() for cafe in searched_cafe])
    else:
        return jsonify(error={
            "Not Found": "Sorry we dont have a cafe at that location"
        }), 404

@app.route("/add", methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
    # if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price"), 200
    # else:
    except:
        return jsonify(error={"NotFound": "Sorry a cafe with that id was not found in the database"}), 404


@app.route("/report-delete/<cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    user_api = request.args.get("api-key")
    if user_api == "TopSecretKey":
        try:
            cafe_to_delete = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success="Successfully deleted the price"), 200
        except:
            return jsonify(error={"NotFound": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error="Sorry that's not allowed make sure you have the correct api-key"), 403

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
