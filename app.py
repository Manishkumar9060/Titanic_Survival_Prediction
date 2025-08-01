from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("titanic_model.joblib")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    fare = float(request.form['fare'])

    sex_numeric = 1 if sex.lower() == 'male' else 0
    input_data = [[pclass, sex_numeric, fare]]
    prediction = model.predict(input_data)[0]
    result = "🟢 Survived" if prediction == 1 else "🔴 Did Not Survive"

    return render_template(
        'index.html',
        prediction_text=f"Prediction: {result}",
        pclass_value=pclass,
        sex_value=sex,
        fare_value=fare
    )

if __name__ == '__main__':
    app.run(debug=True)
