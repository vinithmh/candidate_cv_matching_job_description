#!/usr/bin/env python
# coding: utf-8

# ## Cosine Similarity and CV Ranking Utilities

# In[6]:


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_cosine_similarity(job_description, cv_embeddings):
    job_description = np.array(job_description).reshape(1, -1)
    similarities = cosine_similarity(job_description, cv_embeddings)
    return similarities

def rank_pdfs_by_similarity(sel_job_desp_df, dataframes, position_title_mapping):
    dataframes_with_ranks = {}
    
    for position_title, job_description in zip(sel_job_desp_df['position_title'], sel_job_desp_df['job_description']):
        job_description_embeddings = np.array(job_description).reshape(1, -1)
        cv_df = dataframes[position_title_mapping[position_title]]
        cv_embeddings = np.array(list(cv_df['Details']))
        
        similarities = calculate_cosine_similarity(job_description_embeddings, cv_embeddings)
        pdf_file_names = cv_df['PDF File Name']
        
        ranked_pdf_file_names = [pdf_file_names[i] for i in np.argsort(similarities[0])[::-1]]
        
        rank_df = pd.DataFrame({'PDF File Name': ranked_pdf_file_names,
                                'Cosine Similarity': similarities[0][np.argsort(similarities[0])[::-1]]})
        
        dataframes_with_ranks[position_title] = rank_df
    
    return dataframes_with_ranks

def find_top_5_cvs(sel_job_desp_df, dataframes, position_title_mapping):
    top_5_cvs = {}
    for position_title, job_description in zip(sel_job_desp_df['position_title'], sel_job_desp_df['job_description']):
        job_description_embeddings = extract_distilbert_embeddings(job_description)
        cv_df = dataframes[position_title_mapping[position_title]]
        cv_embeddings = np.array(list(cv_df['Details']))
        similarities = calculate_cosine_similarity(job_description_embeddings, cv_embeddings)
        pdf_file_names = cv_df['PDF File Name']
        ranked_pdf_file_names = [pdf_file_names[i] for i in np.argsort(similarities[0])[-1:-6:-1]]
        top_5_cvs[position_title] = ranked_pdf_file_names
    return top_5_cvs

