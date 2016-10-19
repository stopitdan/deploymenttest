from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    # gold = request.session['gold']
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activity' in request.session:
        request.session['activity'] = []
    return render(request, 'gold/index.html')

def process_money(request):
    if request.method == 'POST':
        date = datetime.datetime.now().strftime(' %B %d, %Y ')
        if request.POST['action'] == 'farm':
            gold_added = random.randint(10,20)
            date = datetime.datetime.now()
            request.session['gold'] += gold_added
            request.session['activity'].append('Earned {} gold from the farm! ({})'.format(gold_added, date))
        elif request.POST['action'] == 'cave':
            gold_added = random.randint(5,10)
            date = datetime.datetime.now()
            request.session['gold'] += gold_added
            request.session['activity'] += ['Earned {} gold from the cave! ({})'.format(gold_added, date)]
        elif request.POST['action'] == 'house':
            gold_added = random.randint(2,5)
            date = datetime.datetime.now()
            request.session['gold'] += gold_added
            request.session['activity'] += ['Earned {} gold from the house! ({})'.format(gold_added, date)]
        elif request.POST['action'] == 'casino':
            gold_added = random.randint(-50,50)
            date = datetime.datetime.now()
            request.session['gold'] += gold_added
            request.session['activity'] += ['Earned {} gold from the casino! ({})'.format(gold_added, date)]
    return redirect(index)

def reset(request):
    print "Reseting Game!"
    del request.session['gold']
    del request.session['activity']
    return redirect('/')

# import random
# import datetime
# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)
# app.secret_key = 'thisissecret'
#
# @app.route('/')
# def index():
#     if 'gold' not in session:
#         session['gold'] = 0
#     if 'activity' not in session:
#         session['activity'] = ""
#     return render_template("index.html")
#
# @app.route('/process_money', methods=['POST'])
# def process_money():
#     if request.form['action'] == 'farm':
#         gold_added = random.randint(10,20)
#         date = datetime.datetime.now()
#         session['gold'] += gold_added
#         session['activity'] += 'Earned {} gold from the farm! ({})'.format(str(gold_added), date)
#     if request.form['action'] == 'cave':
#         gold_added = random.randint(5,10)
#         session['gold'] += gold_added
#         date = datetime.datetime.now()
#         session['activity'] += 'Earned {} gold from the cave! ({})'.format(str(gold_added), date)
#     if request.form['action'] == 'house':
#         gold_added = random.randint(2,5)
#         session['gold'] += gold_added
#         date = datetime.datetime.now()
#         session['activity'] += 'Earned {} gold from the house! ({})'.format(str(gold_added), date)
#     if request.form['action'] == 'casino':
#         gold_added = random.randint(-50,50)
#         session['gold'] += gold_added
#         date = datetime.datetime.now()
#         if gold_added > -1:
#             session['activity'] += 'Earned {} gold from the casino! ({})'.format(str(gold_added), date)
#         else:
#             session['activity'] += 'Lost {} gold from the casino! ({})'.format(str(gold_added), date)
#     return redirect('/')
#
# @app.route('/reset', methods=['POST'])
# def reset():
#     print("Resetting game")
#     del session['gold']
#     del session['activity']
#     return redirect('/')
# app.run(debug=True)
