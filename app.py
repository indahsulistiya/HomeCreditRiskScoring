import joblib
import streamlit as st
import numpy as np

# loading the trained model
loaded_model = joblib.load('model_decision_tree_dataset_feature_selection_oversampling.pkl')

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(NAME_CONTRACT_TYPE, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN, AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY, AMT_GOODS_PRICE, NAME_TYPE_SUITE, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, REGION_POPULATION_RELATIVE, DAYS_BIRTH,  FLAG_MOBIL , FLAG_CONT_MOBILE, FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS, REG_REGION_NOT_LIVE_REGION, REG_REGION_NOT_WORK_REGION, LIVE_REGION_NOT_WORK_REGION, ORGANIZATION_TYPE, APARTMENTS_AVG, YEARS_BEGINEXPLUATATION_AVG, APARTMENTS_MODE, YEARS_BEGINEXPLUATATION_MODE, YEARS_BEGINEXPLUATATION_MEDI, APARTMENTS_MEDI, OBS_30_CNT_SOCIAL_CIRCLE, AMT_REQ_CREDIT_BUREAU_YEAR):

 # Pre-processing user input    
    if NAME_CONTRACT_TYPE == "Cash":
        NAME_CONTRACT_TYPE = 0
    else:
        NAME_CONTRACT_TYPE = 1
 
    if CODE_GENDER == "F":
        CODE_GENDER = 0
    elif CODE_GENDER == "M":
        CODE_GENDER = 1
    elif CODE_GENDER == "XNA":
        CODE_GENDER = 2

    if FLAG_OWN_CAR == "N":
        FLAG_OWN_CAR = 0
    else:
        FLAG_OWN_CAR = 1
        
    if FLAG_OWN_REALTY == "N":
        FLAG_OWN_REALTY = 0
    else:
        FLAG_OWN_REALTY = 1
        
    if NAME_TYPE_SUITE == "Children":
        NAME_TYPE_SUITE = 0
    elif NAME_TYPE_SUITE == "Family":
        NAME_TYPE_SUITE = 1
    elif NAME_TYPE_SUITE == "Group of people":
        NAME_TYPE_SUITE = 2
    elif NAME_TYPE_SUITE == "Other_A":
        NAME_TYPE_SUITE = 3
    elif NAME_TYPE_SUITE == "Other_B":
        NAME_TYPE_SUITE = 4
    elif NAME_TYPE_SUITE == "Spouse, partner":
        NAME_TYPE_SUITE = 5
    elif NAME_TYPE_SUITE == "Unaccompanied":
        NAME_TYPE_SUITE = 6
        
    if NAME_INCOME_TYPE == "Businessman":
        NAME_INCOME_TYPE = 0
    elif NAME_INCOME_TYPE == "Commercial associate":
        NAME_INCOME_TYPE = 1
    elif NAME_INCOME_TYPE == "Maternity leave":
        NAME_INCOME_TYPE = 2
    elif NAME_INCOME_TYPE == "Pensioner":
        NAME_INCOME_TYPE = 3
    elif NAME_INCOME_TYPE == "State servant":
        NAME_INCOME_TYPE = 4
    elif NAME_INCOME_TYPE == "Student":
        NAME_INCOME_TYPE = 5
    elif NAME_INCOME_TYPE == "Unemployed":
        NAME_INCOME_TYPE = 6
    elif NAME_INCOME_TYPE == "Working":
        NAME_INCOME_TYPE = 7
        
    if NAME_EDUCATION_TYPE == "Academic degree":
        NAME_EDUCATION_TYPE = 0
    elif NAME_EDUCATION_TYPE == "Higher education":
        NAME_EDUCATION_TYPE = 1
    elif NAME_EDUCATION_TYPE == "Incomplete higher":
        NAME_EDUCATION_TYPE = 2
    elif NAME_EDUCATION_TYPE == "Lower secondary":
        NAME_EDUCATION_TYPE = 3
    elif NAME_EDUCATION_TYPE == "Secondary / secondary special":
        NAME_EDUCATION_TYPE = 4
        
    if NAME_FAMILY_STATUS == "Civil marriage":
        NAME_FAMILY_STATUS = 0
    elif NAME_FAMILY_STATUS == "Married":
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == "Separated":
        NAME_FAMILY_STATUS = 2
    elif NAME_FAMILY_STATUS == "Single / not married":
        NAME_FAMILY_STATUS = 3
    elif NAME_FAMILY_STATUS == "Unknown":
        NAME_FAMILY_STATUS = 4
    elif NAME_FAMILY_STATUS == "Widow":
        NAME_FAMILY_STATUS = 5
        
    if NAME_HOUSING_TYPE == "Co-op apartment":
        NAME_HOUSING_TYPE = 0
    elif NAME_HOUSING_TYPE == "House / apartment":
        NAME_HOUSING_TYPE = 1
    elif NAME_HOUSING_TYPE == "Municipal apartment":
        NAME_HOUSING_TYPE = 2
    elif NAME_HOUSING_TYPE == "Office apartment":
        NAME_HOUSING_TYPE = 3
    elif NAME_HOUSING_TYPE == "Rented apartment":
        NAME_HOUSING_TYPE = 4
    elif NAME_HOUSING_TYPE == "With parents":
        NAME_HOUSING_TYPE = 5
        
    if OCCUPATION_TYPE == "Accountants":
        OCCUPATION_TYPE = 0
    elif OCCUPATION_TYPE == "Cleaning staff":
        OCCUPATION_TYPE = 1
    elif OCCUPATION_TYPE == "Cooking staff":
        OCCUPATION_TYPE = 2
    elif OCCUPATION_TYPE == "Core staff":
        OCCUPATION_TYPE = 3
    elif OCCUPATION_TYPE == "Drivers":
        OCCUPATION_TYPE = 4
    elif OCCUPATION_TYPE == "HR staff":
        OCCUPATION_TYPE = 5
    elif OCCUPATION_TYPE == "High skill tech staff":
        OCCUPATION_TYPE = 6
    elif OCCUPATION_TYPE == "IT staff":
        OCCUPATION_TYPE = 7
    elif OCCUPATION_TYPE == "Laborers":
        OCCUPATION_TYPE = 8
    elif OCCUPATION_TYPE == "Low-skill Laborers":
        OCCUPATION_TYPE = 9
    elif OCCUPATION_TYPE == "Managers":
        OCCUPATION_TYPE = 10
    elif OCCUPATION_TYPE == "Medicine staff":
        OCCUPATION_TYPE = 11
    elif OCCUPATION_TYPE == "Private service staff":
        OCCUPATION_TYPE = 12
    elif OCCUPATION_TYPE == "Realty agents":
        OCCUPATION_TYPE = 13
    elif OCCUPATION_TYPE == "Sales staff":
        OCCUPATION_TYPE = 14
    elif OCCUPATION_TYPE == "Secretaries":
        OCCUPATION_TYPE = 15
    elif OCCUPATION_TYPE == "Security staff":
        OCCUPATION_TYPE = 16
    elif OCCUPATION_TYPE == "Waiters/barmen staff":
        OCCUPATION_TYPE = 17
        
    if ORGANIZATION_TYPE == "Advertising":
        ORGANIZATION_TYPE = 0
    elif ORGANIZATION_TYPE == "Agriculture":
        ORGANIZATION_TYPE = 1
    elif ORGANIZATION_TYPE == "Bank":
        ORGANIZATION_TYPE = 2
    elif ORGANIZATION_TYPE == "Business Entity Type 1":
        ORGANIZATION_TYPE = 3
    elif ORGANIZATION_TYPE == "Business Entity Type 2":
        ORGANIZATION_TYPE = 4
    elif ORGANIZATION_TYPE == "Business Entity Type 3":
        ORGANIZATION_TYPE = 5
    elif ORGANIZATION_TYPE == "Cleaning":
        ORGANIZATION_TYPE = 6
    elif ORGANIZATION_TYPE == "Construction":
        ORGANIZATION_TYPE = 7
    elif ORGANIZATION_TYPE == "Culture":
        ORGANIZATION_TYPE = 8
    elif ORGANIZATION_TYPE == "Electricity":
        ORGANIZATION_TYPE = 9
    elif ORGANIZATION_TYPE == "Emergency":
        ORGANIZATION_TYPE = 10
    elif ORGANIZATION_TYPE == "Government":
        ORGANIZATION_TYPE = 11
    elif ORGANIZATION_TYPE == "Hotel":
        ORGANIZATION_TYPE = 12
    elif ORGANIZATION_TYPE == "Housing":
        ORGANIZATION_TYPE = 13
    elif ORGANIZATION_TYPE == "Industry: type 1":
        ORGANIZATION_TYPE = 14
    elif ORGANIZATION_TYPE == "Industry: type 10":
        ORGANIZATION_TYPE = 15
    elif ORGANIZATION_TYPE == "Industry: type 11":
        ORGANIZATION_TYPE = 16
    elif ORGANIZATION_TYPE == "Industry: type 12":
        ORGANIZATION_TYPE = 17
    elif ORGANIZATION_TYPE == "Industry: type 13":
        ORGANIZATION_TYPE = 18
    elif ORGANIZATION_TYPE == "Industry: type 2":
        ORGANIZATION_TYPE = 19
    elif ORGANIZATION_TYPE == "Industry: type 3":
        ORGANIZATION_TYPE = 20
    elif ORGANIZATION_TYPE == "Industry: type 4":
        ORGANIZATION_TYPE = 21
    elif ORGANIZATION_TYPE == "Industry: type 5":
        ORGANIZATION_TYPE = 22
    elif ORGANIZATION_TYPE == "Industry: type 6":
        ORGANIZATION_TYPE = 23
    elif ORGANIZATION_TYPE == "Industry: type 7":
        ORGANIZATION_TYPE = 24
    elif ORGANIZATION_TYPE == "Industry: type 8":
        ORGANIZATION_TYPE = 25
    elif ORGANIZATION_TYPE == "Industry: type 9":
        ORGANIZATION_TYPE = 26
    elif ORGANIZATION_TYPE == "Insurance":
        ORGANIZATION_TYPE = 27
    elif ORGANIZATION_TYPE == "Kindergarten":
        ORGANIZATION_TYPE = 28
    elif ORGANIZATION_TYPE == "Legal Services":
        ORGANIZATION_TYPE = 29
    elif ORGANIZATION_TYPE == "Medicine":
        ORGANIZATION_TYPE = 30
    elif ORGANIZATION_TYPE == "Military":
        ORGANIZATION_TYPE = 31
    elif ORGANIZATION_TYPE == "Mobile":
        ORGANIZATION_TYPE = 32
    elif ORGANIZATION_TYPE == "Other":
        ORGANIZATION_TYPE = 33
    elif ORGANIZATION_TYPE == "Police":
        ORGANIZATION_TYPE = 34
    elif ORGANIZATION_TYPE == "Postal":
        ORGANIZATION_TYPE = 35
    elif ORGANIZATION_TYPE == "Realtor":
        ORGANIZATION_TYPE = 36
    elif ORGANIZATION_TYPE == "Religion":
        ORGANIZATION_TYPE = 37
    elif ORGANIZATION_TYPE == "Restaurant":
        ORGANIZATION_TYPE = 38
    elif ORGANIZATION_TYPE == "School":
        ORGANIZATION_TYPE = 39
    elif ORGANIZATION_TYPE == "Security":
        ORGANIZATION_TYPE = 40
    elif ORGANIZATION_TYPE == "Security Ministries":
        ORGANIZATION_TYPE = 41
    elif ORGANIZATION_TYPE == "Self-employed":
        ORGANIZATION_TYPE = 42
    elif ORGANIZATION_TYPE == "Services":
        ORGANIZATION_TYPE = 43
    elif ORGANIZATION_TYPE == "Telecom":
        ORGANIZATION_TYPE = 44
    elif ORGANIZATION_TYPE == "Trade: type 1":
        ORGANIZATION_TYPE = 45
    elif ORGANIZATION_TYPE == "Trade: type 2":
        ORGANIZATION_TYPE = 46
    elif ORGANIZATION_TYPE == "Trade: type 3":
        ORGANIZATION_TYPE = 47
    elif ORGANIZATION_TYPE == "Trade: type 4":
        ORGANIZATION_TYPE = 48
    elif ORGANIZATION_TYPE == "Trade: type 5":
        ORGANIZATION_TYPE = 49
    elif ORGANIZATION_TYPE == "Trade: type 6":
        ORGANIZATION_TYPE = 50
    elif ORGANIZATION_TYPE == "Trade: type 7":
        ORGANIZATION_TYPE = 51
    elif ORGANIZATION_TYPE == "Transport: type 1":
        ORGANIZATION_TYPE = 52
    elif ORGANIZATION_TYPE == "Transport: type 2":
        ORGANIZATION_TYPE = 53
    elif ORGANIZATION_TYPE == "Transport: type 3":
        ORGANIZATION_TYPE = 54
    elif ORGANIZATION_TYPE == "Transport: type 4":
        ORGANIZATION_TYPE = 55
    elif ORGANIZATION_TYPE == "University":
        ORGANIZATION_TYPE = 56
    elif ORGANIZATION_TYPE == "XNA":
        ORGANIZATION_TYPE = 57
 
    # Making predictions 
    
    prediction = loaded_model.predict([[NAME_CONTRACT_TYPE, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN, AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY, AMT_GOODS_PRICE, NAME_TYPE_SUITE, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, REGION_POPULATION_RELATIVE, DAYS_BIRTH,  FLAG_MOBIL , FLAG_CONT_MOBILE, FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS, REG_REGION_NOT_LIVE_REGION, REG_REGION_NOT_WORK_REGION, LIVE_REGION_NOT_WORK_REGION, ORGANIZATION_TYPE, APARTMENTS_AVG, YEARS_BEGINEXPLUATATION_AVG, APARTMENTS_MODE, YEARS_BEGINEXPLUATATION_MODE, YEARS_BEGINEXPLUATATION_MEDI, APARTMENTS_MEDI, OBS_30_CNT_SOCIAL_CIRCLE, AMT_REQ_CREDIT_BUREAU_YEAR]])
     
    if prediction == 0:
        pred = 'Client with fluent payments'
    else:
        pred = 'Client with payment difficulties'
    return pred
      
  
    # this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    st.title("Deploying Machine Learning Models to Predict Home Credit Risk Scoring")
    from PIL import Image
    img = Image.open('about-us-home-credit.jpg')
    img = img.resize((700, 418))
    st.image(img, use_column_width=False)
    st.caption("by : Kelompok 16 Accelerated Machine Learning Program PZSIB x Kampus Merdeka")
 
    
    html_temp = """ 
    <div style ="background-color:grey;padding:13px"> 
    <h1 style ="color:white;text-align:center;">HOME CREDIT RISK SCORING</h1> 
    <h2 style ="color:white;text-align:center;">predict how capable each applicant is of repaying a loan</h2> 
    </div> 
    
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    st.subheader("Isi formulir di bawah ini dengan teliti!!")
    
    NAME_CONTRACT_TYPE = st.radio('Name Contract Type', ("Cash loans", "Revolving loans"))
    
    CODE_GENDER = st.radio('Gender',("F","M", "XNA"))
    
    DAYS_BIRTH = st.number_input("Days Birth (Age)")
    
    FLAG_OWN_CAR = st.radio('Flag Own Car : did client have a car?',("N","Y"))
    
    FLAG_OWN_REALTY = st.radio('Flag Own Realty : did client have a house or flat?',("N","Y"))
    
    CNT_CHILDREN = st.number_input("Count Children")
    
    AMT_INCOME_TOTAL = st.number_input("Amount Income Total")
    
    AMT_CREDIT = st.number_input("Amount Credit")
    
    AMT_ANNUITY = st.number_input("Amount Annuity")
    
    AMT_GOODS_PRICE = st.number_input("Amount Goods Price")
    
    NAME_TYPE_SUITE = st.radio('Name Type Suite (Who was accompanying client when he was applying for the loan)',("Children", "Family", "Group of people", "Other_A", "Other_B", "Spouse Partner", "Unaccompanied"))
    
    NAME_INCOME_TYPE = st.radio('Name Income Type',("Businessman", "Commercial associate", "Maternity Leave", "Pensioner", "State servant", "Student", "Unemployed", "Working"))
    
    NAME_EDUCATION_TYPE = st.radio('Name Education Type (Level of highest education the client)',("Academic degree", "Higher education", "Incomplete higher", "Lower secondary", "Secondary / secondary special"))
    
    NAME_FAMILY_STATUS = st.radio('Name Family Status',("Civil marriage", "Married", "Separated", "Single / not married", "Unknown", "Widow"))
    
    NAME_HOUSING_TYPE = st.radio('Name Housing Type',("Co-op apartment", "House / apartment", "Municipal apartment", "Office apartment", "Rented apartment", "With parents"))
    
    REGION_POPULATION_RELATIVE = st.number_input('Region Population Relative : population of region where client lives (higher number means the client lives in more populated region)')
    
    FLAG_MOBIL = st.radio('Did client provide mobile phone? (1=YES, 0=NO)',(0,1))
    
    FLAG_CONT_MOBILE = st.radio('Was mobile phone reachable? (1=YES, 0=NO)',(0,1))
 
    FLAG_EMAIL = st.radio('Did client provide email? (1=YES, 0=NO)',(0,1))
    
    OCCUPATION_TYPE = st.radio('Occupation Type',("Accountants", "Cleaning staff" , "Cooking staff", "Core staff" , "Drivers", "HR staff", "High skill tech staff", "IT staff", "Laborers", "Low-skill Laborers", "Managers", "Medicine staff", "Private service staff", "Realty agents", "Sales staff", "Secretaries", "Security staff", "Waiters/barmen staff"))
    
    CNT_FAM_MEMBERS = st.number_input("Count Family Members")
    
    REG_REGION_NOT_LIVE_REGION = st.radio('Did client permanent address does not match contact address? (1=different, 0=same, at region level)',(0,1))
    
    REG_REGION_NOT_WORK_REGION = st.radio('Did client permanent address does not match work address? (1=different, 0=same, at region level)',(0,1))
    
    LIVE_REGION_NOT_WORK_REGION = st.radio('Did client contact address does not match work address? (1=different, 0=same, at region level)',(0,1))
    
    ORGANIZATION_TYPE = st.radio('Organization Type',("Advertising", "Agriculture", "Bank", "Business Entity Type 1", "Business Entity Type 2", "Business Entity Type 3", "Cleaning","Construction", "Culture", "Electricity", "Emergency", "Government", "Hotel", "Housing", "Industry: type 1", "Industry: type 10", "Industry: type 11", "Industry: type 12", "Industry: type 13", "Industry: type 2", "Industry: type 3", "Industry: type 4", "Industry: type 5", "Industry: type 6", "Industry: type 7", "Industry: type 8", "Industry: type 9", "Insurance", "Kindergarten", "Legal Services", "Medicine", "Military", "Mobile", "Other", "Police", "Postal", "Realtor", "Religion", "Restaurant", "School", "Security", "Security Ministries", "Self-employed", "Services", "Telecom", "Trade: type 1", "Trade: type 2", "Trade: type 3", "Trade: type 4", "Trade: type 5","Trade: type 6", "Trade: type 7", "Transport: type 1", "Transport: type 2", "Transport: type 3", "Transport: type 4", "University", "XNA" ))
    
    APARTMENTS_AVG = st.number_input('Apartments Average')
    
    YEARS_BEGINEXPLUATATION_AVG =  st.number_input('Years Begin Expluatation Average')
    
    APARTMENTS_MODE = st.number_input('Apartments Mode')
    
    YEARS_BEGINEXPLUATATION_MODE = st.number_input('Years Begin Expluatation Mode')
    
    YEARS_BEGINEXPLUATATION_MEDI = st.number_input('Years Begin Expluatation Median')
    
    APARTMENTS_MEDI = st.number_input('Apartments Median')
    
    OBS_30_CNT_SOCIAL_CIRCLE = st.number_input('How many observation of client social surroundings with observable 30 DPD (days past due) default?')
    
    AMT_REQ_CREDIT_BUREAU_YEAR = st.number_input('Number of enquiries to Credit Bureau about the client one day year (excluding last 3 months before application)')
  
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("predict"): 
        result = prediction(NAME_CONTRACT_TYPE, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN, AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY, AMT_GOODS_PRICE, NAME_TYPE_SUITE, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, REGION_POPULATION_RELATIVE, DAYS_BIRTH,  FLAG_MOBIL , FLAG_CONT_MOBILE, FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS, REG_REGION_NOT_LIVE_REGION, REG_REGION_NOT_WORK_REGION, LIVE_REGION_NOT_WORK_REGION, ORGANIZATION_TYPE, APARTMENTS_AVG, YEARS_BEGINEXPLUATATION_AVG, APARTMENTS_MODE, YEARS_BEGINEXPLUATATION_MODE, YEARS_BEGINEXPLUATATION_MEDI, APARTMENTS_MEDI, OBS_30_CNT_SOCIAL_CIRCLE, AMT_REQ_CREDIT_BUREAU_YEAR) 
        st.success('the predicted result is : {}'.format(result))
        
        
        st.balloons()
     
if __name__=='__main__': 
    main()