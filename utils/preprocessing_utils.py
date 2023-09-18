# preprocessing_utils.py

import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK's stop words and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Preprocess text by following these steps:
    1. Remove punctuation characters and newline characters.
    2. Convert text to lowercase for consistent capitalization.
    3. Tokenize the text into words.
    4. Remove common stopwords (e.g., 'the', 'is') using NLTK's stopwords list.
    5. Apply lemmatization to reduce words to their base form.

    Args:
        text (str): The input text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    # Step 1: Remove punctuation characters and newline characters
    punctuation_pattern = re.compile(r'[{}]'.format(re.escape(string.punctuation)))
    cleaned_text = punctuation_pattern.sub('', text)
    cleaned_text = cleaned_text.replace('\n', '')

    # Step 2: Convert to lowercase
    cleaned_text = cleaned_text.lower()

    # Step 3: Tokenize the text into words
    words = nltk.word_tokenize(cleaned_text)

    # Step 4: Remove stopwords and Step 5: Apply lemmatization
    words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]

    # Rejoin the words to form cleaned text
    cleaned_text = ' '.join(words)

    return cleaned_text