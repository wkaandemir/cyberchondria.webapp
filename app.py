# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'ModelXGBoost.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    Marriage = int(request.form['Marriage'])
    Child = int(request.form['Child'])
    Newspaper = int(request.form['Newspaper'])
    Occupation = int(request.form['Occupation'])
    Education = int(request.form['Education'])
    Health_Payment = int(request.form['Health_Payment'])
    Economic_Status = float(request.form['Economic_Status'])
    Chronic_Illnes = int(request.form['Chronic_Illnes'])
    Health_Insurance = int(request.form['Health_Insurance'])
    Emergency_Room = int(request.form['Emergency_Room'])        
    Hospital = int(request.form['Hospital']) 
    Doktor_Visit = int(request.form['Doktor_Visit']) 
    Nutritionist = int(request.form['Nutritionist']) 
    

    input_data = np.array([age, gender, Marriage, Child, Newspaper, Occupation, Education, Health_Payment,Economic_Status,Chronic_Illnes,Health_Insurance,Emergency_Room,Hospital,Nutritionist,Doktor_Visit]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction == 1:
        return render_template('result.html', prediction_text="High Cyberchondria Tendency")
    else:
        return render_template('result.html', prediction_text="Low Cyberchondria Tendency")





if __name__ == '__main__':
	app.run(debug=True)
      
