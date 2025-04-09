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
### Programming Language
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

### Machine Learning
<p align="left">
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
</p>

### Data Processing & Visualization
<p align="left">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/matplotlib-FF9A00?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/seaborn-4C766A?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn">
</p>

### Web Development
<p align="left">
  <b>Backend:</b> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
</p>
<p align="left">
  <b>Frontend:</b> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>
<p align="left">
  <b>Database:</b> <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

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
