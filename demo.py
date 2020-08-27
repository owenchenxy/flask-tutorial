#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<color>')
def color(color):
    default_style = 'style/default_style.html'
    if color != 'red' and color != 'green':
        style_html = default_style
    else:
        style_html = 'style/{0}_style.html'.format(color)
    parameter = {
        'color': color,
        'style_html': style_html,
    }
    return render_template('color.html', **parameter)

if __name__=='__main__':
	app.run(debug=True)