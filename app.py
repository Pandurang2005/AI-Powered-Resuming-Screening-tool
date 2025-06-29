import streamlit as st
import pandas as pd
from resume_parser import parse_resume
from ranker import rank_resumes
from utils import read_job_description, save_uploaded_files

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("🤖 AI-Powered Resume Screening Tool")

# Upload job description
st.header("1. Upload Job Description")
job_desc_file = st.file_uploader("Upload a .txt file for the job description", type=["txt"])

# Upload resumes
st.header("2. Upload Candidate Resumes (PDF)")
resume_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if job_desc_file and resume_files:
    with st.spinner("Processing resumes..."):
        job_description = read_job_description(job_desc_file)
        saved_paths = save_uploaded_files(resume_files)
        parsed_resumes = [parse_resume(path) for path in saved_paths]

        ranked_df = rank_resumes(parsed_resumes, job_description)

    st.success("Resumes ranked successfully!")
    st.dataframe(ranked_df)

    csv = ranked_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Ranked Results as CSV", data=csv, file_name='ranked_resumes.csv', mime='text/csv')
else:
    st.info("Please upload both a job description and at least one resume.")