import random
from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "The Grand Wahzoo will now make a guess."

# count = 0

@app.route('/')
def index():
    # Get computer's random guess
    if 'comp_guess' and 'count' not in session:
        session['comp_guess'] = random.randint(1, 100)
        print(f"computer guess is: {session['comp_guess']}")
        session['user_guess'] = 0
        session['count'] = 0
        session['hide'] = False
    return render_template('index.html')

@app.route('/user_guess', methods=['POST'])
def save_user_guess():
    session['user_guess'] = int(request.form['user_guess'])
    print(f"user guess is: {session['user_guess']}")
    session['count'] += 1
    if session['user_guess'] == session['comp_guess'] or session['count'] == 5:
        session['hide'] = True
    return redirect('/')

@app.route('/end_session')
def end_session():
    session.clear()
    return redirect('/')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
