from flask import Flask, render_template, request, session, redirect, jsonify
import requests
import random
import html

app = Flask(__name__)
app.secret_key = "kbc-secret-key"

# Fallback questions in case API fails
fallback_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Shakespeare", "Homer", "Tolstoy", "Dante"],
        "correct": "Shakespeare"
    },
]

def get_question():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple", headers=headers, timeout=5)
        data = response.json()

        if data.get('response_code') != 0 or 'results' not in data:
            raise ValueError("Invalid API response")

        q = data['results'][0]
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        options = [html.unescape(opt) for opt in q['incorrect_answers']]
        options.append(correct)
        random.shuffle(options)

        return {
            'question': question,
            'options': options,
            'correct': correct
        }

    except Exception as e:
        print("Error loading question:", e)
        fallback = random.choice(fallback_questions)
        return fallback

@app.route("/")
def home():
    session['score'] = 0
    session['lifelines'] = {'skip': True, 'fifty': True}
    return redirect("/quiz")

@app.route("/quiz")
def quiz():
    q = get_question()
    session['correct_answer'] = q['correct']
    session['current_options'] = q['options']

    return render_template(
        "quiz_game.html",
        question=q['question'],
        options=q['options'],
        lifelines=session['lifelines'],
        score=session['score']
    )

@app.route("/answer", methods=["POST"])
def answer():
    user_ans = request.form.get("option")
    correct = session.get('correct_answer')

    if user_ans == correct:
        session['score'] += 10
        if session['score'] >= 120:
            return redirect("/winner")
        return redirect("/quiz")
    else:
        return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", score=session.get('score', 0))

@app.route("/winner")
def winner():
    return render_template("winner.html", score=session.get('score', 0))

@app.route("/lifeline/skip")
def lifeline_skip():
    if session['lifelines'].get('skip', False):
        session['lifelines']['skip'] = False
        return redirect("/quiz")
    return redirect("/quiz")


@app.route("/lifeline/fifty")
def lifeline_fifty():
    if session['lifelines'].get('fifty', False):
        session['lifelines']['fifty'] = False
        correct = session.get('correct_answer')
        options = session.get('current_options', [])
        wrongs = [opt for opt in options if opt != correct]
        remove = random.sample(wrongs, 2)
        return jsonify({"remove": remove})
    return jsonify({"remove": []})

    return redirect("/quiz")

if __name__ == "__main__":
    app.run(debug=True)
