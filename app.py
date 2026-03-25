import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

# Title
st.title("Student Performance & Behavior Predictor")

# Dataset
data = {
    "Hours_Studied": [2, 4, 6, 8, 5, 7],
    "Sleep_Hours": [6, 7, 5, 8, 6, 7],
    "Attendance": [60, 75, 85, 90, 70, 88],
    "Previous_Marks": [40, 50, 65, 80, 55, 75],
    "Important_Qns": [1, 2, 3, 4, 2, 3],
    "Marks": [45, 55, 70, 90, 60, 85],
    "Cheating": [1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Features
X = df[["Hours_Studied", "Sleep_Hours", "Attendance", "Previous_Marks", "Important_Qns"]]

# Models
model_marks = LinearRegression()
model_marks.fit(X, df["Marks"])

model_cheat = LogisticRegression()
model_cheat.fit(X, df["Cheating"])

# User Inputs
st.subheader("Enter Student Details")

hours = st.slider("Study Hours", 0, 12)
sleep = st.slider("Sleep Hours", 0, 12)
attendance = st.slider("Attendance (%)", 0, 100)
prev = st.slider("Previous Marks", 0, 100)
imp = st.slider("Important Questions Answered", 0, 10)

# Prediction Button
if st.button("Predict"):
    new_data = pd.DataFrame({
        "Hours_Studied": [hours],
        "Sleep_Hours": [sleep],
        "Attendance": [attendance],
        "Previous_Marks": [prev],
        "Important_Qns": [imp]
    })

    marks_pred = model_marks.predict(new_data)
    cheat_pred = model_cheat.predict(new_data)

    st.subheader("Results")

    st.write(f"Predicted Marks: {marks_pred[0]:.2f}")

    if marks_pred[0] > 75:
        st.success("Performance: Good")
    else:
        st.warning("Performance: Needs Improvement")

    if cheat_pred[0] == 1:
        st.error("⚠️ Possible Cheating Detected")
    else:
        st.success("✅ No Cheating Detected")
