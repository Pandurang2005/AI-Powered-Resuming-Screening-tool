import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resumes, job_description):
    texts = [res['text'] for res in resumes]
    texts.append(job_description)

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(texts)
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    results = []
    for i, resume in enumerate(resumes):
        results.append({
            'File': resume['file_path'].split('/')[-1],
            'Score': round(cosine_similarities[i], 3)
        })
    return pd.DataFrame(sorted(results, key=lambda x: x['Score'], reverse=True))