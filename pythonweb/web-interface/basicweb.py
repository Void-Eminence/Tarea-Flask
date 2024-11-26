# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template, send_from_directory
from user_agents import parse
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('license.html')

@app.route('/browser')
def browser():
    
    ipaddr = request.environ['REMOTE_ADDR']
    uadata = parse(request.user_agent.string)
    return render_template('about.html', title='Datos del Navegador', ipaddr=ipaddr, uastr=str(uadata))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')