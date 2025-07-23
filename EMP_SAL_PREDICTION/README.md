
# 💼 Employee Salary Prediction App

A Machine Learning web application that predicts whether an employee earns **more than 50k** or **less than or equal to 50k** per year based on input features such as age, education, occupation, hours worked per week, and years of experience.

---

## 🚀 Features

- Predict salary class (>50k or <=50k) for a single employee using input form.
- Batch prediction by uploading a CSV file.
- Clean and responsive UI using **Streamlit**.
- Best model saved and used for inference (`best_model.pkl`).

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend/Modeling**: Python, Scikit-learn, Pandas, NumPy  
- **Deployment (Local)**: Pyngrok for secure tunnel (optional)  
- **Model Serialization**: Joblib

---

## 📁 Dataset

- **Source**: UCI Adult Income Dataset  
- **Columns Used**:  
  - `age`  
  - `education`  
  - `occupation`  
  - `hours-per-week`  
  - `experience`  
  - `salary` (Target)

---

## 🔁 Project Workflow

1. **Data Preprocessing**  
   - Clean missing values (`?`)  
   - Remove irrelevant features  
   - Encode categorical variables  
   - Scale numerical values  

2. **Model Building**  
   - Algorithms tried: Logistic Regression, Random Forest, KNN, SVM, Gradient Boosting  
   - Selected best based on accuracy  
   - Saved using `joblib`

3. **Web App Development**  
   - Built with Streamlit  
   - Sliders and dropdowns for easy input  
   - CSV upload for batch processing  

---

## 🧪 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/employee-salary-prediction.git
   cd employee-salary-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. (Optional) To make it publicly accessible:
   ```bash
   pyngrok http 8501
   ```

---

## 📸 Screenshot

![App Screenshot](screenshots/streamlit_ui.png)

---

## 📂 Folder Structure

```
employee-salary-prediction/
├── app.py
├── best_model.pkl
├── data/
│   └── adult.csv
├── utils/
│   └── preprocess.py
├── requirements.txt
└── README.md
```

---

## 📌 Future Improvements

- Add cloud deployment (e.g., Streamlit Cloud, Heroku)
- Add login/auth for secure access
- Model explainability using SHAP

---

## 👨‍💻 Author

Mahesh Jorige  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)
