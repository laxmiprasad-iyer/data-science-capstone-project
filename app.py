import streamlit as st
import pickle
import numpy as np

st.title('Car selling price prediction')
st.header('Fill the details to generate car selling price prediction')

option=st.sidebar.selectbox('Select the model',['Linear Regression','Bagging Linear Regression','KNN Regression',
                'Bagging KNN Regression','Decision Tree Regression','Bagging Decision Tree Regression',
                'Ridge Regression','Lasso Regression','Random Forest Regression','Ada Boost Regression',
                'Gradient Boosting Regression','XGBoost Regression'])

if option == 'Linear Regression':
    with open('lr.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Bagging Linear Regression':
    with open('bag_lr.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'KNN Regression':
    with open('kn_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Bagging KNN Regression':
    with open('bag_kn.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Decision Tree Regression':
    with open('dt_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Bagging Decision Tree Regression':
    with open('clf.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Ridge Regression':
    with open('rg_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Lasso Regression':
    with open('ls_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Random Forest Regression':
    with open('rf_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'AdaBoost Regression':
    with open('ab_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'Gradient Boosting Regression':
    with open('gr_rs.pkl','rb') as f:
        model=pickle.load(f)
elif option == 'XGBoost Regression':
    with open('xg_rs.pkl','rb') as f:
        model=pickle.load(f)



brand_types=['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
       'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
       'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
       'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
       'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia']

brand_Maruti=0
brand_Hyundai=0
brand_Datsun=0
brand_Honda=0
brand_Tata=0
brand_Chevrolet=0
brand_Toyota=0
brand_Jaguar=0
brand_Mercedes_Benz=0
brand_Audi=0
brand_Skoda=0
brand_Jeep=0
brand_BMW=0
brand_Mahindra=0
brand_Ford=0
brand_Nissan=0
brand_Renault=0
brand_Fiat=0
brand_Volkswagen=0
brand_Volvo=0
brand_Mitsubishi=0
brand_Land=0
brand_Daewoo=0
brand_MG=0
brand_Force=0
brand_Isuzu=0
brand_OpelCorsa=0
brand_Ambassador=0
brand_Kia=0

brand=st.selectbox('Select the brand',brand_types)

if brand == 'Mercedes-Benz': # we have to deal with hyphens and spaces since variable names do not allow these characters
    brand='Mercedes_Benz'

exec('brand_'+brand+'=1')


km_driven=int(st.text_input('KM Driven',0))

fuel_types=['Petrol','Diesel','CNG','LPG','Electric']

fuel_Petrol=0
fuel_Diesel=0
fuel_CNG=0
fuel_LPG=0
fuel_Electric=0

fuel=st.selectbox('Select fuel',fuel_types)

exec('fuel_'+fuel+'=1')


seller_type_types=['Individual','Dealer','Trustmark Dealer']

seller_type_Individual=0
seller_type_Dealer=0
seller_type_Trustmark_Dealer=0

seller_type = st.selectbox('Seller Type',seller_type_types)

if seller_type == 'Trustmark Dealer':
    seller_type='Trustmark_Dealer'

exec('seller_type_'+seller_type+'=1')


transmission_types=['Manual','Automatic']

transmission_Manual=0
transmission_Automatic=0

transmission= st.selectbox('Transmission',transmission_types)

exec('transmission_'+transmission+'=1')


year=int(st.text_input('Model Year',2005))

owner_types=['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car']

owner_First_Owner=0
owner_Second_Owner=0
owner_Third_Owner=0
owner_Fourth_Above_Owner=0
owner_Test_Drive_Car=0

owner=st.selectbox('Owner',owner_types)

if owner == 'First Owner':
    owner_First_Owner=1
elif owner == 'Second Owner':
    owner_Second_Owner=1
elif owner == 'Third Owner':
    owner_Third_Owner=1
elif owner == 'Fourth & Above Owner':
    owner_Fourth_Above_Owner=1
else:
    owner_Test_Drive_Car=1


vect=[year,km_driven,fuel_CNG,fuel_Diesel,fuel_Electric,fuel_LPG,fuel_Petrol,seller_type_Dealer,seller_type_Individual,seller_type_Trustmark_Dealer,transmission_Automatic,transmission_Manual,
      owner_First_Owner,owner_Fourth_Above_Owner,owner_Second_Owner,owner_Test_Drive_Car,owner_Third_Owner,brand_Ambassador,
      brand_Audi,brand_BMW,brand_Chevrolet,brand_Daewoo,brand_Datsun,brand_Fiat,brand_Force,brand_Ford,brand_Honda,brand_Hyundai,
      brand_Isuzu,brand_Jaguar,brand_Jeep,brand_Kia,brand_Land,brand_MG,brand_Mahindra, brand_Maruti,brand_Mercedes_Benz,
      brand_Mitsubishi,brand_Nissan,brand_OpelCorsa,brand_Renault,brand_Skoda,brand_Tata,brand_Toyota,brand_Volkswagen,brand_Volvo]

print(vect)
input=np.array(vect).reshape(1,46)

if st.button('Predict'):
    t=model.predict(input)[0]
    if t < 0:
        t=50000
    st.success(t)



