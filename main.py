import numpy as np
from flask import Flask, jsonify, render_template, request
import pickle
import sklearn

app = Flask(__name__)

model = pickle.load(open('LoanPrediction.pkl','rb'))

@app.route('/test',methods=['GET'])
def test():
    return "Test request received successfully. Service is running."

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        ApplicantIncome = request.form['Applicant Income']
        CoapplicantIncome = request.form['Co Applicant Income']
        LoanAmount = request.form['Loan Amount']
        Loan_Amount_Term = request.form['Loan Amount Term']
        Gender = request.form['Gender']
        Married = request.form['Married']
        Dependents = request.form['Dependents']
        Education = request.form['Education']
        Self_Employed = request.form['Self employed']
        Credit_History = request.form['Credit History']
        property_area_type = request.form['Property Area Type']
        Urban=0
        Semiurban=0
        Rural=0
        #Assigning values to Urban, Rural and Semiurban depending on user's input
        if(property_area_type == "Urban"):
            Urban = 1
            Semiurban = 0
            Rural = 0
        elif(property_area_type == "Semiurban"):
            Urban = 0
            Semiurban = 1
            Rural = 0
        else:
            Urban = 0
            Semiurban = 0
            Rural = 1


        data = [int(Gender),int(Married), int(Dependents), int(Education), int(Self_Employed),
        int(ApplicantIncome), int(CoapplicantIncome), int(LoanAmount), int(Loan_Amount_Term),
        int(Credit_History), int(Rural), int(Semiurban),int(Urban)]
        
        print(data)
        #prob = model.predict_proba([data])
        pred = model.predict([[int(Gender),int(Married), int(Dependents), int(Education), int(Self_Employed),
        int(ApplicantIncome), int(CoapplicantIncome), int(LoanAmount), int(Loan_Amount_Term),
        int(Credit_History), int(Rural), int(Semiurban),int(Urban)]])
        
        print(pred)
        print(pred[0])
        status=""
        #print(prob)
        if(pred[0]==0):
            status = "REJECTED"
        else:
            status = "APPROVED"
        
        return render_template('index.html', prediction_text="LOAN STATUS: {}".format(status))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
