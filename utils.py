import os

def read_job_description(file):
    return file.read().decode('utf-8')

def save_uploaded_files(uploaded_files):
    folder = 'uploaded_resumes'
    os.makedirs(folder, exist_ok=True)
    saved_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(folder, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.read())
        saved_paths.append(file_path)
    return saved_paths