from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Power_Type_Diesel=0
    Brand_Name_Usha=0
    if request.method == 'POST':
        Market_Price=float(request.form['Market_Price'])
        Power_Type_Electric=request.form['Power_Type_Electric']
        if(Power_Type_Electric=='Electric'):
                Power_Type_Electric=1
                Power_Type_Battery=0
        else:
            Power_Type_Electric=0
            Power_Type_Battery=1
        Brand_Name_Khaitan=request.form['Brand_Name_Khaitan']
        if(Brand_Name_Khaitan=='Khaitan'):
                Brand_Name_Khaitan=1
                Brand_Name_Usha=0
        else:
            Brand_Name_Khaitan=0
            Brand_Name_Usha=1
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        prediction=model.predict([[Market_Price,Power_Type_Electric,Brand_Name_Usha,Brand_Name_Khaitan,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="You cannot sell this fan")
        else:
            return render_template('index.html',prediction_text="You Can Sell the fan  at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

