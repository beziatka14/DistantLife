from flask import Blueprint, render_template, session


views = Blueprint('views', __name__)


@views.route('/')
def main():
    return render_template("main.html")

@views.errorhandler(404)
def page_not_found():
    return render_template("error_404.html"), 404
