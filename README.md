# 🌱 Crop Recommendation System

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Project-green)](https://croplife-ds6-project.onrender.com/)

A machine learning-based web application to recommend the best crops for agricultural fields based on soil nutrients and weather conditions.

---

## 🚀 Features
- **Soil Analysis**: Input N, P, K, pH levels of your soil.
- **Weather Integration**: Uses temperature, humidity, and rainfall data.
- **Smart Recommendations**: ML model suggests top 3 suitable crops.
- **Farmer-Friendly Interface**: Simple Django web app for easy use.

---

## 🛠️ Technologies Used
- **Python** (Backend Logic)
- **Django** (Web Framework)
- **scikit-learn** (Random Forest ML Model)
- **pandas & NumPy** (Data Processing)
- **SQLite** (Database)
- **HTML/CSS/JavaScript** (Frontend)

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/manjurul369/Crop-Recommendation-System.git
   cd Crop-Recommendation-System

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
 
4. Run migrations:

   ```bash
   python manage.py migrate
   
5. Start the Django server:

   ```bash
   python manage.py runserver
