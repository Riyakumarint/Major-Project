from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        Irradiance = int(request.form['Irradiance'])
        Resistance=float(request.form['Resistance'])
        I1 = float(request.form['I1'])
        V1 = float(request.form['V1'])
        I2 = float(request.form['I2'])
        V2 = float(request.form['V2'])
        I3 = float(request.form['I3'])
        V3 = float(request.form['V3'])
        I4 = float(request.form['I4'])
        V4 = float(request.form['V4'])
        I5 = float(request.form['I5'])
        V5 = float(request.form['V5'])
        I6 = float(request.form['I6'])
        V6 = float(request.form['V6'])

        prediction=model.predict([[Irradiance,Resistance,I1,V1,I2,V2,I3,V3,I4,V4,I5,V5,I6,V6]])
        n = 0
        temp = 0.0
        for i in range(5):
            if (prediction[0, i] > temp):
                temp = prediction[0, i]
                n = i
        faults = ["Fault : No Fault", "Fault : Short Circuit Fault", "Fault : Degradation", "Fault : Open Circuit Fault", "Fault : Partial Shadow"]

        return render_template('index.html', prediction_text=faults[n])
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

