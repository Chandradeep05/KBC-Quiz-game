# 🌟 KBC Quiz Game Web Application

An interactive web-based quiz game inspired by *Kaun Banega Crorepati (KBC)*, built using **Flask**, **HTML/CSS**, and **JavaScript**. The game allows users to play through 12 questions, use lifelines (50:50, Skip), and receive a final score with a winner screen upon successful completion.

---

## 🚀 Features

* 🌟 Dynamic quiz questions fetched from the Open Trivia DB API
* ✅ 50:50 lifeline – hides two incorrect options
* ⏭️ Skip lifeline – allows the user to skip a question
* 💡 Real-time scoring and game progression
* 🎉 Winner screen after answering 12 questions correctly
* ⚠️ Game over screen with score on incorrect answer

---

## 🛠️ Technologies Used

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **API:** [Open Trivia DB](https://opentdb.com/api_config.php)
* **Templating Engine:** Jinja2

---

## 🧠 How It Works

1. User visits the homepage and begins the quiz.
2. Each question is dynamically loaded from the Trivia API.
3. Lifelines can be used once per game:

   * **50:50** (removes two wrong answers)
   * **Skip** (bypasses the current question)
4. If the user answers 12 questions correctly, they win the game.
5. A wrong answer ends the game and displays the final score.

---

## 📷 Screenshots

# **Quiz Screen**


<img width="748" height="614" alt="image" src="https://github.com/user-attachments/assets/53d4f004-2755-4318-88ef-6ce22597a3b0" />

# **Winner Screen**


<img width="766" height="502" alt="image" src="https://github.com/user-attachments/assets/cd408510-5ab5-44be-9ef2-eac2ba81f068" />


# **Game over Screen**


<img width="608" height="489" alt="image" src="https://github.com/user-attachments/assets/5f2ebb30-95b2-45de-8521-8ec5439defc6" />

---

## 📦 Installation & Run

```bash
git clone https://github.com/yourusername/kbc-quiz-game.git
cd kbc-quiz-game
pip install -r requirements.txt
python quiz_game.py
```

Visit: `http://127.0.0.1:5000/`

---

## 📄 License

MIT License
