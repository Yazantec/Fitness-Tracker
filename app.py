import streamlit as st
st.set_page_config(
    page_title="Fitness Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Personal Fitness Tracker")
st.markdown("Track your fitness, calculate calories, and get our recommendations!")
st.sidebar.header("User Information")
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=74)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=220, value=170)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=20)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
body_fat_known = st.sidebar.checkbox("I know my Body Fat %")
if body_fat_known:
    body_fat = st.sidebar.slider("Body Fat %", min_value=5, max_value=50, value=18)
else:
    body_fat = None
activity_level = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active",]
)
height_m = height / 100
bmi = weight / (height_m ** 2)
if gender == "Male":
    bmr = 10*weight + 6.25*height - 5*age + 5
else:
    bmr = 10*weight + 6.25*height - 5*age - 161
activity_multipliers = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
}
tdee = bmr * activity_multipliers[activity_level]
st.header("Your Fitness Stats")
st.metric("BMI", f"{bmi:.1f}")
st.metric("BMR (Calories/day)", f"{bmr:.0f}")
st.metric("TDEE (Calories/day)", f"{tdee:.0f}")
st.header("Our Recommendations")
if body_fat:
    if body_fat < 15:
        st.success("Low body fat. Focus on building muscle and maintaining nutrition.")
    elif 15 <= body_fat < 25:
        st.success("Healthy body fat range! Keep up the good work.")
    else:
        st.warning("High body fat. Focus on diet and cardio for health.")
else:
    if bmi < 18.5:
        st.success("You are underweight. Focus on muscle gain and balanced nutrition.")
    elif 18.5 <= bmi < 25:
        st.success("You are in a healthy range! Maintain consistency in training and diet.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight. Consider reducing calories and adding cardio.")
    else:
        st.error("Obese range. Consult a professional for guidance and focus on health.")
st.subheader("Recommended Daily Macros")
protein = weight * 2      # 2g per kg
fat = weight * 0.8         # 0.8g per kg
carbs = (tdee - (protein*4 + fat*9)) / 4
st.write(f"Protein: {protein:.0f}g | Fat: {fat:.0f}g | Carbs: {carbs:.0f}g")
st.markdown("---")
st.markdown("Coach yazan | Your Wellness, Our Priority!")
import streamlit as st

st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="💪",
    layout="wide"
)

st.image("thumbnail.png", use_container_width=True)

st.title("💪 Fitness Tracker")
st.write("Track your workouts and progress easily!")

