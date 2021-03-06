#!/usr/env/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.appconfig import AppConfig
import flask_ink.ink as ink

def create_app(configfile=None):
    app = Flask('sample_app')
    AppConfig(app, configfile)

    ink.Ink(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    create_app('config.cfg').run(host='0.0.0.0')
