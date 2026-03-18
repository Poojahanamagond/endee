import streamlit as st

# Sample resumes
resumes = [
    "Java developer with Spring Boot and MySQL experience",
    "Frontend developer with React and JavaScript skills",
    "Python developer with AI and Machine Learning knowledge"
]

st.title("AI Resume Search 🔍")

query = st.text_input("Enter your search:")

if st.button("Search"):
    if query:
        # simple matching logic
        best_match = None
        for resume in resumes:
            if query.lower() in resume.lower():
                best_match = resume
                break
        
        if best_match:
            st.subheader("Best Match Resume:")
            st.write(best_match)
        else:
            st.write("No exact match found")
    else:
        st.write("Enter something")