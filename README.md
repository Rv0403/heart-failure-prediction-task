

---

# ❤️ Heart Failure Prediction 

A machine learning-powered web app that predicts the risk of heart disease using patient health data. Built with Random Forest and deployed using Streamlit.

## 🔗 Live Demo

🚀 [Click here to try the app](https://heart-failure-prediction-task.streamlit.app)

📦 [View on GitHub](https://github.com/Rv0403/heart-failure-prediction-task)

---

## 📂 Dataset

* Format: CSV with medical attributes such as age, cholesterol, chest pain type, etc.

---

## 🧪 Exploratory Data Analysis (EDA)

✔️ Checked for **null values**
📊 Counted and plotted unique values for categorical features
📈 Plotted histograms for continuous features
🚫 Detected and removed **outliers** (e.g., Cholesterol = 0)

---

## 🧹 Data Preprocessing

* **Label Encoding**: Applied to all categorical columns (`Sex`, `ChestPainType`, etc.)
* **Scaling**: Skipped (Random Forest doesn't require it)

---

## 🤖 Model Building

* Tried multiple models:

  * Logistic Regression
  * Decision Tree
  * XGBoost
  * Random Forest
* Performed **Grid Search CV** (no significant improvement)
* ✅ Final Model: **Random Forest Classifier**

  * **Accuracy**: `~89.2%`

---

## 💾 Model Export

* Saved the trained model and encoders using `pickle`

  * `model.pkl`
  * `encoders.pkl`

---

## 🌐 Web App Interface

Built with **Streamlit**:

* Form-based UI for input
* Predicts `Heart Disease` or `No Heart Disease`
* Encodes categorical inputs using saved encoders

### 🔧 Run locally

```bash
git clone https://github.com/your-username/heart-failure-prediction
cd heart-failure-prediction
pip install -r requirements.txt
streamlit run Heart_Failure_prediction.py
```

---

## 🗂️ Project Structure

```
├── Task.ipynb                   # Jupyter notebook with EDA + training
├── Heart_Failure_prediction.py  # Streamlit web app
├── model.pkl                    # Trained model
├── encoders.pkl                 # LabelEncoders
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

---

## 📈 Future Improvements

* Add feature importance plots
* Include performance metrics (precision, recall, F1-score)
* Accept CSV uploads for bulk predictions
* Enhance UI for better user guidance

---
