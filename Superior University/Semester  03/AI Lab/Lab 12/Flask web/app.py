
from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.metrics import accuracy_score

app = Flask(__name__)
model = pickle.load(open('model_svc.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = request.form['features']
        true_label = request.form['true_label']
        features = np.array([float(x) for x in features.split(',')]).reshape(1, -1)
        true_label = int(true_label)
        prediction = model.predict(features)[0]
        accuracy = accuracy_score([true_label], [prediction])

        return render_template(
            'index.html',
            prediction_text=f'Predicted Class: {prediction}',
            accuracy_text=f'Accuracy: {round(accuracy, 3)}'
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
