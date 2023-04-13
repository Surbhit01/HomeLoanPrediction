import streamlit as st
import pickle
#from styles import streamlit_style

#streamlit_style()

#model = pickle.load(open('LoanPrediction.pkl','rb'))
pickle_in = open("LoanPrediction.pkl","rb")
model=pickle.load(pickle_in)

def main():
    #st.title("Home Loan Predictor")
    html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Home Loan Predictor</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)    
    
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = st.number_input("Co Applicant Income",min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0)
    Loan_Amount_Term = st.number_input("Loan Amount Term (in months)", min_value=0)
    self_Employed = st.radio('Self Employed', ('Yes', 'No'))
    credit_History = st.radio('Does Credit History meet requirements', ('Yes', 'No'))
    dependents = st.selectbox("No of Dependents",('0','1','2','3+'))
    gender = st.radio('Gender', ('Male', 'Female'))
    married = st.radio('Married', ('Yes', 'No'))
    education = st.radio('Education', ('Graduate', 'Not Graduate'))
    property_area_type = st.selectbox('Property Area', ('Urban','Rural','Semiurban'))

    if st.button("Predict"):
        print('Button pressed')

        #Self Employed
        if self_Employed == "Yes":
            Self_Employed = 1
        else:
            Self_Employed = 0

        #credit History
        if credit_History == "Yes":
            Credit_History = 1
        else:
            Credit_History = 0

        #Dependents
        if dependents == "0":
            Dependents = 0
        elif dependents == "1":
            Dependents = 1
        elif dependents == "2":
            Dependents = 2
        else:
            Dependents = 3   

        #Gender
        if gender == "Male":
            Gender = 1
        else:
            Gender = 0

        #Married
        if married == "Yes":
            Married = 1
        else:
            Married = 0

        #Education
        if education == "Graduate":
            Education = 1
        else:
            Education = 0

        #Property Area Type
        if property_area_type == "Urban":
            Urban = 1
            Semiurban = 0
            Rural = 0
        elif property_area_type == "Semiurban":
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

        pred = model.predict([[int(Gender),int(Married), int(Dependents), int(Education), int(Self_Employed),
        int(ApplicantIncome), int(CoapplicantIncome), int(LoanAmount), int(Loan_Amount_Term),
        int(Credit_History), int(Rural), int(Semiurban),int(Urban)]])
        #print(pred)
        print(pred[0])
        if pred[0] == 0:
            result = """<h2>Loan Rejected</h2>"""
        else:
            result = """<h2>Loan Accepted</h2>"""

        st.markdown(result, unsafe_allow_html=True)


if __name__=='__main__':
    main()