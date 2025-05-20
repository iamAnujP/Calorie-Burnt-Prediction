from flask import Flask, render_template, request
from model import predict_calories

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    r2 = mae = mse = rmse = None  # Initialize metrics

    if request.method == 'POST':
        gender = 0 if request.form['gender'] == 'Male' else 1
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])
        heart_rate = float(request.form['heart_rate'])
        body_temp = float(request.form['body_temp'])

        # Get prediction and metrics
        prediction, r2, mae, mse, rmse = predict_calories(
            gender, age, height, weight, duration, heart_rate, body_temp
        )

    return render_template(
        'index.html',
        prediction=prediction,
        r2=r2,
        mae=mae,
        mse=mse,
        rmse=rmse
    )

if __name__ == '__main__':
    app.run(debug=True)
