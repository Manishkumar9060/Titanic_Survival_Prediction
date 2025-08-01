# 🚢 Titanic Survival Prediction 

A machine learning web application built with **Flask** and **Python** that predicts whether a passenger survived the Titanic disaster based on their travel class, gender, and fare.  
The model is trained using the Titanic dataset and deployed with an interactive frontend for user input.

---

## 🔧 Tech Stack
- **Backend**: Python, Flask, Joblib
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Machine Learning**: Scikit-learn, ML Tecnique 
- **Dataset**: Titanic Dataset (Pclass, Sex, Fare → Survived)

---

## 📌 Features
- User-friendly interface with Titanic-themed background
- Predicts survival probability based on:
  - Passenger Class (`Pclass`)
  - Gender (`Sex`)
  - Ticket Fare (`Fare`)
- Responsive design for mobile and desktop
- Pre-filled form values after submission until page refresh
- Clears prediction and inputs when the user refreshes manually

---

## 🚀 How It Works
1. User enters passenger details in the form
2. Flask backend processes input and sends it to the trained ML model
3. The model predicts **Survived 🟢** or **Did Not Survive 🔴**
4. Prediction and input values remain until page refresh

---

## 🖥️ Installation & Run
```bash
git clone https://github.com/yourusername/titanic-survival-prediction.git
cd titanic-survival-prediction
pip install -r requirements.txt
python app.py

**## Preview of Titanic Survival Prediction**
<img width="1904" height="860" alt="image" src="https://github.com/user-attachments/assets/480d2a0e-2137-4f5e-84cd-c1099654f2d5" />

