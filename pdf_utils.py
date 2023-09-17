#!/usr/bin/env python
# coding: utf-8

# ## PDF Text Extraction Utilities 

# In[1]:


import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file_path):
    doc = fitz.open(pdf_file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def extract_job_role_from_pdf(pdf_file_path):
    job_role = ""
    try:
        pdf_text = extract_text_from_pdf(pdf_file_path)
        # Extract first line (Job Role)
        job_role = pdf_text.split('\n')[0].strip()
    except Exception as e:
        print(f"Error extracting job role from {pdf_file_path}: {str(e)}")
    return job_role

def extract_skills_from_pdf(pdf_file_path):
    # ... (continue with skills extraction)
    pass

def extract_education_from_pdf(pdf_file_path):
    # ... (continue with education extraction)
    pass

