#!/usr/bin/env python
# coding: utf-8

# ## Data Processing and NLP Utilities

# In[4]:


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK's stop words and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Tokenize, remove stop words, and lemmatize the text
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]
    return ' '.join(words)

def remove_punctuation(text):
    # Remove punctuation from text
    return re.sub(r'[^\w\s]', '', text)

def remove_newlines(text):
    # Remove newline characters from text
    return text.replace('\n', ' ')

def convert_to_lowercase(text):
    # Convert text to lowercase
    return text.lower()

