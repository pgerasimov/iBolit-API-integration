import logging

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    logging.basicConfig(filename='app.log',
                        filemode='w',
                        level=logging.ERROR,
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        format='%(name)s - %(levelname)s - %(message)s')

    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response

    @app.route("/")
    def index():
        return render_template('base.html', active='index')

    return app
