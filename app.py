from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de ejemplo
events = [
    {"id": 1, "team1": "FCBarcelona", "team2": "Bayern Munich", "odds1": 2.2, "odds2": 2.5},
    {"id": 2, "team1": "RB Leipzig", "team2": "Liverpool", "odds1": 1.8, "odds2": 2.2},
    {"id": 3, "team1": "Benfica", "team2": "Feyernoord", "odds1": 2.0, "odds2": 1.6}
]

@app.route('/')
def home():
    return render_template('index.html', events=events)

@app.route('/bet', methods=['POST'])
def bet():
    event_id = int(request.form['event_id'])
    team = request.form['team']
    amount = float(request.form['amount'])
    # Aquí añadirías la lógica para procesar la apuesta
    return f"Apuesta realizada en el evento {event_id} por {amount} euros al equipo {team}."


@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/submit-encuesta', methods=['POST'])
def submit_encuesta():
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    # Procesa las respuestas de la encuesta
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
