# Home Loan Prediction

## PROBLEM STATEMENT
Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and then the company validates the customer loan eligiblity. The company wants to automate the loan eligibility process (real time) based on customer detail provided while filling the online loan application form. The details which are required in the application form are - Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others.

To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers.

## APPROACH
* The dataset with 11 features like Gender, number of dependents, Loan Amount etc was analysed. 
* Based on the values of the features, appropriate data processing was done.
* Used Random Forest to build the model for prediction. This model(.pkl) was depoyed on [Google Cloud Platform](http://homeloanprediction.appspot.com/)

Vizualized different factors and how their effect on the probablity of loan being approved.

![Gender~Count](https://user-images.githubusercontent.com/24591039/219856862-57f1b56e-9437-40fe-ba7c-5e376b0e88fe.png)

[Image Above] Gender~Loan Status count plot

![Dependents~Count](https://user-images.githubusercontent.com/24591039/219856873-fb7efee0-326d-406f-a2ce-c1615d69f922.png)

[Image Above] No of Dependents~Loan Status count plot

![Edu~count](https://user-images.githubusercontent.com/24591039/219856874-476cc29e-5184-484b-925c-b21534ab3ae9.png)

[Image Above] Education Level~Loan Status count plot

![Married~Count](https://user-images.githubusercontent.com/24591039/219856875-06424721-1fea-40c4-9a97-c56c3fc3cf62.png)

[Image Above] Marital Status~Loan Status count plot

![Property Area~Count](https://user-images.githubusercontent.com/24591039/219856876-b7f4fdae-2bf6-44c4-ba43-a07b11876d47.png)

[Image Above] Property Area Type~Loan Status count plot

![Self employed~count](https://user-images.githubusercontent.com/24591039/219856877-1752c9df-2440-4cd8-b667-30c70e47b505.png)

[Image Above] Self Employed~Loan Status count plot

![featureImp](https://user-images.githubusercontent.com/24591039/219857357-96759608-8325-4566-a5a6-d8b51268365d.png)

[Image Above] Feature Importance

![Error model](https://user-images.githubusercontent.com/24591039/219857504-13648f62-2c53-4817-abe4-687592055fdb.png)

[Image Above] Error Term Analysis for Random Forest on test data

![HomePage](https://user-images.githubusercontent.com/24591039/219857530-571a4a14-50fa-42d0-af49-254ff7425b17.png)

[Image Above] Deployment Home Page

