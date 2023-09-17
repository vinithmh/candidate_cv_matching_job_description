#!/usr/bin/env python
# coding: utf-8

# ## BERT Embedding Extraction Utilities

# In[5]:


import torch
from transformers import DistilBertTokenizer, DistilBertModel

# Initialize DistilBERT model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

def extract_distilbert_embeddings(text):
    # Tokenize text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    # Generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    # Extract embeddings for the [CLS] token
    cls_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return cls_embedding

