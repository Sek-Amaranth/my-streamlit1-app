import streamlit as st

st.title("โปรแกรมคำนวณ BMI")
 
weight = st.number_input("น้ำหนัก (กก.)", 1.0)
height = st.number_input("ส่วนสูง (ซม.)", 100.0)
 
if height > 0:
    bmi = weight / ((height/100)**2)
    st.write(f"BMI ของคุณคือ: {bmi:.2f}")
 
    if bmi < 18.5:
         st.warning("ผอมเกินไป")
    elif bmi < 25:
         st.success("น้ำหนักปกติ")
    else:
         st.error("อ้วน")



