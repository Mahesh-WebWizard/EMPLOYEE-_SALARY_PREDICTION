# EMPLOYEE_SALARY_PREDICTION_USING_KNN

A beginner-friendly machine learning project that predicts whether an employee’s salary is **greater than 50K** or **less than or equal to 50K** using the **K-Nearest Neighbors (KNN)** algorithm. This project uses Python, Streamlit for UI, and a CSV file containing employee data.

---

## 📌 What is This Project?

This project:

- Reads employee data from a `.csv` file (like age, education, hours per week, etc.)
- Trains a machine learning model using **KNN (K-Nearest Neighbors)** algorithm
- Predicts the salary class of a new employee based on similar data
- Shows the result on a **user-friendly web app** built using **Streamlit**

---

## 💡 Why Did We Build This?

- To learn how data is used to make predictions
- To understand how machine learning works using a real-world example
- To show how CSV data, ML models, and web apps work together

---

## 🧠 What is KNN?

KNN (K-Nearest Neighbors) is a **machine learning algorithm** that:

- Finds the "K" most similar data points in the dataset
- Predicts the value (like salary class) based on those neighbors

It's simple, intuitive, and often a first algorithm beginners learn.

---

## 🧰 Technologies Used

| Tool/Library   | Purpose                                  |
|----------------|------------------------------------------|
| Python         | Programming Language                     |
| pandas         | Data handling and CSV reading            |
| scikit-learn   | ML algorithm and model building          |
| Streamlit      | Web interface for user input/output      |
| joblib         | Save and load trained models easily      |

---

## 🗂️ Folder Structure

```
EMP_SAL_PRE_USING_KNN/
│
├── emp_using_knn/
│   ├── adult.csv           # Employee dataset
│   ├── knn_model.py        # Code to train the model
│   ├── app.py              # Streamlit app to make predictions
│   └── knn_model.pkl       # Saved trained model (created after training)
│
├── README.md               # Project documentation (this file)
```

---

## 📝 Dataset Info - `adult.csv`

This file contains employee details like:

- Age
- Workclass
- Education
- Occupation
- Hours per week
- Salary class (target: `>50K` or `<=50K`)

---

## ⚙️ How to Run This Project

### ✅ OPTION 1: Manual Setup (No Git)

1. Go to this GitHub page.
2. Click on **Code** → **Download ZIP**
3. Extract the ZIP file.
4. Open the extracted folder.
5. Inside the `emp_using_knn` folder, follow these steps:

```bash
pip install pandas scikit-learn streamlit joblib
```

6. Run the model training file (to generate the model):

```bash
python knn_model.py
```

7. Run the web app:

```bash
streamlit run app.py
```

8. It will open the app in your browser where you can enter employee info and see salary prediction.

---

### ✅ OPTION 2: Using Git (Command Line)

1. Open your terminal or command prompt
2. Run:

```bash
git clone https://github.com/Mahesh-Jorige/EMP_SAL_PRE_USING_KNN.git
cd EMP_SAL_PRE_USING_KNN/emp_using_knn
```

3. Install required libraries:

```bash
pip install pandas scikit-learn streamlit joblib
```

4. Train the model:

```bash
python knn_model.py
```

5. Launch the Streamlit app:

```bash
streamlit run app.py
```

6. App will launch in your browser.

---

## 🖥️ How Does the App Work?

1. You enter inputs like age, workclass, education, etc.
2. The app feeds this data to the KNN model
3. The model predicts salary class:
   - **>50K** → Higher salary
   - **<=50K** → Lower salary

---

## 🔍 Future Improvements

- Use different algorithms like Decision Tree, Random Forest
- Add graphs/visualizations
- Add accuracy report and confusion matrix

---

## 🙋‍♂️ Who Can Use This?

- Beginners learning machine learning
- Students building academic projects
- Anyone curious about data prediction

---

## 🙌 Connect with Me

📇 **Mahesh Jorige**    
Let’s connect, collaborate, or talk tech!

[LinkedIn](https://www.linkedin.com/in/maheshjorige/) | [GitHub](https://github.com/Mahesh-WebWizard)
