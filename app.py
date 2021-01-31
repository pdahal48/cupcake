from flask import Flask, request, jsonify, render_template, redirect
from models import db, connect_db, Cupcake

from cupcake_form import AddcupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route("/",  methods=['GET', 'POST'])
def add_pet():
    """Pet cupcake form; handle adding."""
    
    cupcakes = Cupcake.query.all()
    form = AddcupcakeForm()

    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data 
        image = image if image else None

        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(cupcake)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("index.html", form=form, cupcakes=cupcakes)


@app.route('/api/cupcakes')
def list_cupcakes():
    """ List all of the cupcakes in the database """

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def list_cupcake(id):
    """ List an individual cupcake"""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())



@app.route('/api/cupcakes', methods=['POST'])
def create_cupcakes():
    """ Create new cupcakes"""

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    image = image if image else None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    """ Edit a specific cupcake feature """

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """ Delete a cupcake from the database """

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Cupcake has been deleted')
