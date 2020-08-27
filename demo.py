#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/exam', methods=['GET','POST'])
def exam():
    show_answer = False
    correct1, correct2, correct3 = False, False, False
    if request.method == 'GET':
        return render_template('exam.html', **locals())
    elif request.method == 'POST':
        show_answer = True
        if request.form.get('q1') == '2':
            correct1 = True
        if request.form.get('q2') == '文华学院':
            correct2 = True
        if request.form.get('q3') == '北京':
            correct3 = True
        return render_template('exam.html', **locals())

if __name__=='__main__':
	app.run(debug=True)