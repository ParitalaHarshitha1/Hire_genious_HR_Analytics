import streamlit as st

st.set_page_config(page_title="recruiter", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('HireGenius')

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
<style>
.bigger-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="bigger-font">\U000026A1 Powered by the OpenAI GPT models, this app serves as your personal assistant in the recruitment or job application process! </p>', unsafe_allow_html=True)

st.markdown('<p class="big-font"> <a href="http://localhost:8501/I_am_a_Recruiter"><strong>As a recruiter, you can follow these steps:</strong></a> First, copy and paste the provided job description into the text field. Then, upload the applicants resumes in PDF format. Finally, click the submit button. In return, you will receive a detailed report 📁, complete with a visual chart 📊 that compares the candidates strengths in the essential skills required for the job. This streamlined process will help you quickly identify the top talent for the position!</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font"> <a href="http://localhost:8501/I_am_an_Applicant"><strong>👨‍💼 If you are an applicant, follow these steps:</strong></a> Copy and paste the job description into the text field, upload your resume in PDF format, and hit the submit button! You will receive valuable suggestions 📝 on how to enhance your resume to align better with the job description, helping you stand out as the ideal candidate for the position. 🚀</p>', unsafe_allow_html=True)

#st.markdown('<p class="big-font"> \U0001F4B8 Every time you use this app, I am being charged by the OpenAI API. Please consider donating <a href="https://donate.stripe.com/cN2dUMe379mNcLu9AA">here</a> \U0001F4B0 \U0001F64F</p>', unsafe_allow_html=True)




st.markdown("<small>Created by Harshitha Paritala :pencil2:</small>", unsafe_allow_html=True)
st.markdown("[GitHub](https://github.com/ParitalaHarshitha1)")
st.markdown("[Medium](https://medium.com/@harshithaparitala1)")