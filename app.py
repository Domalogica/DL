#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request, Response
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.contrib.fixers import ProxyFix
import requests, os

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")


@app.route('/')
def main():
    return render_template('index.html')


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)