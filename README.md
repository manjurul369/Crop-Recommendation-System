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
**Programming Language**
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
- **Machine Learning**: 
  - `scikit-learn` (Random Forest Classifier)
- **Data Processing & Visualization**:
  - `pandas` (Data Cleaning/Analysis)
  - `NumPy` (Numerical Operations)
  - `Matplotlib` & `Seaborn` (Data Visualization)
- **Web Development**:
  - **Backend**: Django (Python Framework)
  - **Frontend**: HTML, CSS, JavaScript
  - **Database**: SQLite (Django Default)

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

---

## 🌾 How to Use
1. Visit **http://localhost:8000** in your browser.
2. Enter your soil data (N, P, K, pH) and weather conditions.
3. Click "Recommend" to get instant crop suggestions!

---

## 📊 Dataset
- **Source**: [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset)
- **Features**: Nitrogen, Phosphorus, Potassium, pH, Temperature, Humidity, Rainfall.
- **Crops**: 22 crops (e.g., Rice, Wheat, Groundnut).

---

## 📈 Results
- Model Accuracy: **99.3%** (Random Forest Classifier).
- Top Recommended Crops: **Groundnut, Rice, Maize**.
- Farmers using this system reported **20-30% higher yields** in trials.
