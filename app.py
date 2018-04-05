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

@app.route('/vacancies')
def vacancies():
    return render_template('vacancies.html')

@app.route('/vacancies_msg')
def vacancies_msg():
    return render_template('vacancies_msg.html')


@app.route('/vacancies_msg', methods=['POST','GET'])
def sendMessage():
    _1 = request.form['_1']
    _2 = request.form['_2']
    _3 = request.form['_3']
    _4 = request.form['_4']
    _5 = request.form['_5']
    _6 = request.form['_6']
    _7 = request.form['_7']
    _8 = request.form['_8']
    _9 = request.form['_9']
    _10 = request.form['_10']
    _11 = request.form['_11']
    _12 = request.form['_12']
    _13 = request.form['_13']
    _14 = request.form['_14']
    _15 = request.form['_15']
    _16 = request.form['_16']
    _17 = request.form['_17']
    _18 = request.form['_18']
    _19 = request.form['_19']
    _20 = request.form['_20']
    _21 = request.form['_21']
    _22 = request.form['_22']
    _23 = request.form['_23']
    _24 = request.form['_24']
    _25 = request.form['_25']
    _27 = request.form['_27']
    _29 = request.form['_29']
    _30 = request.form['_30']
    _31 = request.form['_31']
    _32 = request.form['_32']
    _33 = request.form['_33']
    _34 = request.form['_34']
   

    text = """
	Фамилия / Имя / Отчество: %s
	Номер телефона / Электронная почта: %s
	Адрес проживания: %s
	Образование / компетенции: %s
	Желаемые должности / Зарплата: %s
	Место работы: %s



	Чего вы ждете от работы в нашей компании?: %s

	Какие у вас есть опасения, что вас может не устроить в нашей компании?: %s

	Что на прошлой работе, было для Вас интереснее всего?: %s

	От чего на прошлой работе вы получали наибольшее удовлетворение?: %s

	Что вас тяготило на предыдущей работе?: %s

	Что бы вам хотелось изменить в Вашей прошлой работе?: %s

	Какой должна быть работа, чтобы у Вас не ослабевал к ней интерес?: %s

	Что вас больше всего демотивирует?: %s

	Какие виды поощрения Вы цените?: %s

	Чего  по отношению к вам ни в коем случае нельзя делать?: %s

	Как Вас не надо поощрять?: %s

	Какие у вас есть привязанности и обязательства (прошлая работа, учеба, семья и пр.)?: %s

	Хобби, Увлечения?: %s

	Опишите идеального директора?: %s

	Опишите идеальную компанию?: %s

	Чем по вашему хороший сотрудник отличается от плохого?: %s

	Ваши действия в случае несогласия с руководителем?: %s

	В каком направлении вы бы хотели развиваться. Какие навыки прокачать?: %s

	По каким критериям вы бы оценивали ваш труд?: %s

	За что по вашему стоит сразу уволить сотрудника?: %s

	Что может стать причиной вашего увольнения по собственному желанию?: %s

	Как быстро влиться в команду?: %s

	Какие ваши сильные стороны?: %s

	Какие ваши слабые стороны?: %s

	Какая ваша любимая книга и почему?: %s
    """ % (_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15, _16, _17, _18, _19, _20, _21, _22, _23, _24, _25, _27, _29, _30, _31, _32, _33, _34)
   
    print(text)

    if _1 or _2 or _3 or _4 or _5 or _6 or _7 or _8 or _9 or _10 or _11 or _12 or _13 or _14 or _15 or _16 or _17 or _18 or _19 or _20 or _21 or _22 or _23 or _24 or _25 or _27 or _29 or _30 or _31 or _32 or _33 or _34:
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=167315364&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=70025022&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=65472004&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=-303230127&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=34436430&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot541249154:AAFayJ8bZK1uXeEuD1sAqTXxzKAfRu5GtUA/sendMessage?chat_id=27390261&text=%s" % (text)
        requests.post(url) 
    return render_template('index.html')



app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='domalogica.com', port=80)
