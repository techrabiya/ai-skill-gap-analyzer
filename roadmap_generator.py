import streamlit as st

st.set_page_config(page_title="AI Skill Gap Analyzer", page_icon="🗺️", layout="wide")

st.title("🗺️ AI Tech Skill Gap Analyzer & Roadmap Generator")
st.markdown("Developed by **Rabia Khan** | Python & AI Developer")
st.write("Enter your current skills and target tech role to generate a custom AI learning roadmap.")

current_skills = st.text_input("Your Current Skills (e.g., Python, Basic HTML):", "Python")
target_role = st.selectbox("Select Target Role:", ["AI Engineer", "Full Stack Developer", "Data Scientist", "Python Automation Expert"])

if st.button("Generate Roadmap"):
    if not current_skills.strip():
        st.warning("Please enter your current skills.")
    else:
        st.success(f"Roadmap generated successfully for target role: {target_role}!")
        st.metric(label="Readiness Match Score", value="75%")
        st.write("### 📌 Recommended AI Learning Path:")
        st.write("1. Master Advanced Python Data Structures & OOPs.")
        st.write("2. Learn Streamlit Framework for Rapid Web App Deployment.")
        st.write("3. Integrate LLM APIs (OpenAI / Gemini) for intelligent automation.")
        st.balloons()
