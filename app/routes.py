from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from flask import render_template, redirect, url_for, flash, request
from flask import session
from app import app
from app import db
from app.models import Game
from app.forms import GameForm

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/models_and_queries', methods=['GET', 'POST'])
def models_and_queries():
    form = GameForm()
    if form.validate_on_submit():
        try:
            game = Game(
                title = form.title.data,
                genre = form.genre.data,
                rating = form.rating.data
            )
            db.session.add(game)
            db.session.commit()
            flash("Game has been successfully added to database.")
            return redirect(url_for("models_and_queries", form=form))
        except IntegrityError:
            db.session.rollback()
            flash("Entry for this game has already been made.")
            return redirect(url_for("models_and_queries", form=form))

    return render_template("models_and_queries.html", form=form)


@app.route('/list_all_games', methods=["GET", "POST"])
def list_all_games():
    games = Game.query.order_by(Game.title).all()
    return render_template("list_of_games.html", games=games)

@app.route('/delete_game/<int:game_id>', methods=["GET", "POST"])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    flash("You have successfully deleted this game entry!")
    return redirect(url_for('list_all_games'))

@app.route('/update_game/<int:game_id>', methods=['GET', 'POST'])
def update_game(game_id):
    game = Game.query.get_or_404(game_id)
    form = GameForm(obj=game)

    if form.validate_on_submit():
        game.title = form.title.data
        game.genre = form.genre.data
        game.rating = form.rating.data
        db.session.commit()
        flash("You have successfully updated this game!")
        return redirect(url_for("list_all_games"))
    return render_template("update_game.html", form=form)

@app.route('/search_by_genre', methods=['GET', 'POST'])
def search_by_genre():
    query = Game.query
    genre = request.args.get("genre")

    if genre == "rpg":
        query = Game.query.filter(Game.genre == "rpg")
    elif genre == "action":
        query = Game.query.filter(Game.genre == "action")
    elif genre == "horror":
        query = Game.query.filter(Game.genre == "horror")
    elif genre == "multiplayer":
        query = Game.query.filter(Game.genre == "multiplayer")

    games = query.order_by(Game.title).all()
    return render_template("search_by_genre.html", games=games)

