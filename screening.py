def main():
    st.title(" AI-Powered Resume Screening Tool")

    st.subheader("Step 1: Upload Job Description")
    job_desc = st.text_area("Paste the job description here:")

    st.subheader("Step 2: Upload Resumes (PDF)")
    uploaded_files = st.file_uploader("Upload Resumes", type=["pdf"], accept_multiple_files=True)

    if st.button("Run Screening"):
        if job_desc and uploaded_files:
            # Extract & preprocess job description
            job_text = preprocess(job_desc)

            resumes = []
            resume_names = []
            
            for file in uploaded_files:
                resume_text = extract_text_from_pdf(file)
                cleaned_text = preprocess(resume_text)
                resumes.append(cleaned_text)
                resume_names.append(file.name)

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([job_text] + resumes)

            similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

            results = pd.DataFrame({
                "Resume": resume_names,
                "Match Score": (similarity_scores * 100).round(2)
            })

            results = results.sort_values(by="Match Score", ascending=False)

            st.subheader(" Ranked Candidates")
            st.dataframe(results)

            csv = results.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Results as CSV",
                data=csv,
                file_name="resume_screening_results.csv",
                mime="text/csv"
            )

        else:
            st.warning("Please upload both job description and resumes.")

if __name__ == "__main__":
    main()
