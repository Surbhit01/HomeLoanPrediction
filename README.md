# Home Loan Prediction

## PROBLEM STATEMENT
Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and then the company validates the customer loan eligiblity. The company wants to automate the loan eligibility process (real time) based on customer detail provided while filling the online loan application form. The details which are required in the application form are - Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others.

To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers.

## APPROACH
* The dataset with 11 features like Gender, number of dependents, Loan Amount etc was analysed. 
* Based on the values of the features, appropriate data processing was done.
* Used Random Forest to build the model for prediction. This model(.pkl) was depoyed on [Google Cloud Platform](http://homeloanprediction.appspot.com/)
