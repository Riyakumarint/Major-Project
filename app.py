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

    if request.method == 'POST':
        # Irradiance = int(request.form['Irradiance'])
        # Resistance=float(request.form['Resistance'])
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



        # http: // 127.0.0 .1: 5000 / predict /?Irradiance = 1000 & Resistance = 2 & I1 = 0 & V1 = 100 & I2 = 0 & V2 = 100 & I3 = 20 & V3 = 100 & I4 = 20 & V4 = 100 & I5 = 20 & V5 = 100 & I6 = 20 & V6 = 100
        # if key doesn't exist, returns None
        # Irradiance = request.args.get('Irradiance')
        # Resistance = request.args.get('Resistance')
        # I1 = request.args.get('I1')

        prediction=model.predict([[I1,V1,I2,V2,I3,V3,I4,V4,I5,V5,I6,V6]])
        n = 0
        temp = 0.0
        for i in range(5):
            if (prediction[0, i] > temp):
                temp = prediction[0, i]
                n = i
        faults = ["Fault : No Fault", "Fault : Short Circuit fault at string ->", "Fault : Degradation", "Fault : Open Circuit fault at string ->", "Fault : Partial Shadow"]

        a=" "
        if n==1 :
            if (V1 < 0.00001) :
               a+="1, "
            if (V2 < 0.00001) :
               a+="2, "
            if (V3 < 0.00001) :
               a+="3, "
            if (V4 < 0.00001) :
               a+="4, "
            if (V5 < 0.00001) :
               a+="5, "
            if (V6 < 0.00001) :
               a+="6"

        if n==3 :
            if (I1 < 0.00001) :
               a+="1, "
            if (I2 < 0.00001) :
               a+="2, "
            if (I3 < 0.00001) :
               a+="3, "
            if (I4 < 0.00001) :
               a+="4, "
            if (I5 < 0.00001) :
               a+="5, "
            if (I6 < 0.00001) :
               a+="6"



        return render_template('index.html', prediction_text= faults[n] + a )
    else:
        return render_template('index.html', prediction_text="INPUT ERROR")

@app.route("/predictresult", methods=['GET','POST'])
def predictresult():

    if request.method == 'POST':
        # Irradiance = int(request.form['Irradiance'])
        # Resistance=float(request.form['Resistance'])
        # I1 = float(request.form['I1'])
        # V1 = float(request.form['V1'])
        # I2 = float(request.form['I2'])
        # V2 = float(request.form['V2'])
        # I3 = float(request.form['I3'])
        # V3 = float(request.form['V3'])
        # I4 = float(request.form['I4'])
        # V4 = float(request.form['V4'])
        # I5 = float(request.form['I5'])
        # V5 = float(request.form['V5'])
        # I6 = float(request.form['I6'])
        # V6 = float(request.form['V6'])

        # Irradiance = request.args.get('Irradiance',type=int)
        # Resistance = request.args.get('Resistance',type=float)
        I1 = request.args.get('I1',type=float)
        V1 = request.args.get('V1',type=float)
        I2 = request.args.get('I2',type=float)
        V2 = request.args.get('V2',type=float)
        I3 = request.args.get('I3',type=float)
        V3 = request.args.get('V3',type=float)
        I4 = request.args.get('I4',type=float)
        V4 = request.args.get('V4',type=float)
        I5 = request.args.get('I5',type=float)
        V5 = request.args.get('V5',type=float)
        I6 = request.args.get('I6',type=float)
        V6 = request.args.get('V6',type=float)



        # http: // 127.0.0 .1: 5000 / predict /?Irradiance = 1000 & Resistance = 2 & I1 = 0 & V1 = 100 & I2 = 0 & V2 = 100 & I3 = 20 & V3 = 100 & I4 = 20 & V4 = 100 & I5 = 20 & V5 = 100 & I6 = 20 & V6 = 100
        # if key doesn't exist, returns None
        # Irradiance = request.args.get('Irradiance')
        # Resistance = request.args.get('Resistance')
        # I1 = request.args.get('I1')

        prediction=model.predict([[I1,V1,I2,V2,I3,V3,I4,V4,I5,V5,I6,V6]])
        n = 0
        temp = 0.0
        for i in range(5):
            if (prediction[0, i] > temp):
                temp = prediction[0, i]
                n = i
        faults = ["No Fault", "SC at ", "Degradation", "OC at ", "Partial Shadow"]

        a = " "
        if n == 1:
            if (V1 < 0.01):
                a += "1, "
            if (V2 < 0.01):
                a += "2, "
            if (V3 < 0.01):
                a += "3, "
            if (V4 < 0.01):
                a += "4, "
            if (V5 < 0.01):
                a += "5, "
            if (V6 < 0.01):
                a += "6"

        if n == 3:
            if (I1 < 0.01):
                a += "1, "
            if (I2 < 0.01):
                a += "2, "
            if (I3 < 0.01):
                a += "3, "
            if (I4 < 0.01):
                a += "4, "
            if (I5 < 0.01):
                a += "5, "
            if (I6 < 0.01):
                a += "6"

        return faults[n]+a



if __name__=="__main__":
    app.run(debug=True)

