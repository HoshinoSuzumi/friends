# -*- coding: UTF-8 -*-
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    # return redirect('https://github.com/HoshinoSuzumi/issues-api')
    return 'GitHub Issues API'
