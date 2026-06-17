from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('ridge.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = [
            float(request.form['day']),
            float(request.form['month']),
            float(request.form['year']),
            float(request.form['Temperature']),
            float(request.form['RH']),
            float(request.form['Ws']),
            float(request.form['Rain']),
            float(request.form['FFMC']),
            float(request.form['DMC']),
            float(request.form['DC']),
            float(request.form['ISI']),
            float(request.form['BUI']),
            float(request.form['Classes']),
            float(request.form['Region'])
        ]

        final_input = scaler.transform([data])

        prediction = model.predict(final_input)[0]

        return render_template(
            'index.html',
            prediction_text=f'Predicted Fire Weather Index (FWI): {round(prediction,2)}'
        )

    except Exception as e:

        return render_template(
            'index.html',
            prediction_text=f'Error: {e}'
        )

if __name__ == "__main__":
    app.run(debug=True)