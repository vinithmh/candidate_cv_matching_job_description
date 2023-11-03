# Resume Ranking System


## Introduction

The Resume Ranking System is an advanced Python-based project that leverages state-of-the-art Natural Language Processing (NLP) techniques to streamline the process of matching job descriptions with candidate resumes. This project showcases a rich set of skills and capabilities that make it a valuable tool for HR professionals and hiring managers seeking efficient and effective candidate screening.

## Purpose

The primary purpose of the Resume Ranking System is to address the challenges faced during the hiring process, such as:

- Sorting through a large volume of resumes to identify suitable candidates.
- Ensuring that candidate qualifications align with job requirements.
- Minimizing human bias and errors in the candidate screening process.
- Saving time and resources by automating repetitive tasks.

By automating the matching process and providing a data-driven approach, this tool helps organizations identify the most qualified candidates quickly and effectively.

## Key Skills and Capabilities Demonstrated
### 1. Data Extraction from PDFs
   
One of the core functionalities of the Resume Ranking System is its ability to extract vital information from candidate resumes in PDF format. This is achieved using the PyMuPDF library (PyMuPDF is now known as fitz), and it showcases the following skills:

- **PDF Parsing**: The system demonstrates the ability to parse PDF documents efficiently, extracting text data for further analysis.

- **Error Handling**: Robust error handling ensures the project gracefully handles exceptions that may arise during the PDF extraction process.

### 2. Text Data Preprocessing

Before performing any analysis, the system preprocesses both job descriptions and candidate resumes. This step is crucial for ensuring data consistency and meaningful comparisons. Key skills demonstrated include:

- **Text Tokenization**: Utilizing the Hugging Face Transformers library, the system tokenizes text data, preparing it for subsequent analysis.

- **Lowercasing**: Text data is converted to lowercase, ensuring that case sensitivity does not affect similarity calculations.

- **Stopword Removal**: The project employs the NLTK library to remove stopwords from the text, eliminating common words that do not contribute significantly to the analysis.

- **Lemmatization**: The NLTK library is used again for lemmatizing words, reducing inflected words to their base form, and improving analysis accuracy.

### 3. Embeddings and Similarity Calculation
The project incorporates pretrained models, specifically the DistilBERT model from Hugging Face, to convert text data into dense vector representations (embeddings). The system then calculates cosine similarities between job descriptions and candidate resumes. This process showcases:

- **Deep Learning Integration**: Demonstrates the integration of advanced deep learning models, enhancing the project's NLP capabilities.

- **Cosine Similarity**: Utilizes the scikit-learn library to calculate cosine similarity, a fundamental metric for comparing text data.

### 4. Data Organization and Management
The project efficiently organizes and manages data, both for job descriptions and candidate resumes. This demonstrates effective data handling and structuring skills, including:

- **Dataframe Management**: Utilizes the Pandas library to organize and manage data in dataframes, simplifying data manipulation.

- **Dictionary Data Structure**: Uses dictionaries to store and access data, facilitating structured storage for easy retrieval.

### 5. Top Candidate Ranking
The system excels in ranking candidate resumes based on their similarity to job descriptions. This process is crucial for identifying the most suitable candidates for specific positions. Key skills demonstrated include:

- **Dynamic Data Mapping**: The project dynamically maps job titles to corresponding candidate resume datasets, allowing for flexibility and scalability.

- **Ranking Logic**: Utilizes sorting and ranking algorithms to determine the top candidates for each job description, showcasing advanced data analysis capabilities.

## Features

The Job Matching System offers a range of features designed to streamline the hiring process:

- **Data Extraction from PDF Resumes**: The system can extract essential information from candidate resumes in PDF format, including job roles, skills, and education details.

- **Text Preprocessing for Consistency**: It preprocesses both job descriptions and resumes, ensuring consistency and meaningful comparisons by removing noise, stopwords, and inflections.

- **Utilization of pre-trained Models**: Leveraging state-of-the-art pre-trained models like DistilBERT from Hugging Face, the system converts text data into dense vector representations (embeddings).

- **Calculation of Cosine Similarities**: The project calculates cosine similarities between job descriptions and candidate resumes to determine the best fit candidates for each position.

- **Dynamic Data Mapping**: The system dynamically maps job titles to corresponding candidate resume datasets, allowing for flexibility and scalability across industries and job roles.

## Project File Structure

Here is an overview of the project's file structure:

- `data`: Directory containing project data, including candidate ranking and extracted PDF data.
  - `cvs_ranking`: Subdirectory containing candidate ranking data based on cosine similarity.
    - `top_5_cvs.csv`: CSV file listing the top 5 candidates for each job description, ranked by cosine similarity.
       - `pdf_extracted_data`: Subdirectory containing extracted data from PDF files. This may include subdirectories or additional files containing extracted information.
         - `job_descriptions.csv`: CSV file containing job descriptions.
        
- Utils Folder: This folder contains utility functions that can be used across your project. Below is a brief description of each utility file:

   - distilBert_embeddings.py : This file contains utility functions for working with DistilBERT embeddings. It includes functions for extracting embeddings from text using the DistilBERT model.

      - pdf_extract_utils.py : This file contains utility functions for extracting text and information from PDF files. It may include functions for text extraction, metadata extraction, and other PDF-related tasks.

         - preprocessing_utils.py : This file contains utility functions for text preprocessing. It includes functions for removing punctuation, stopwords, and performing other text cleaning tasks to prepare text data for analysis.

            - ranking_utils.py : This file contains utility functions for ranking and similarity calculations. It may include functions for calculating cosine similarity, ranking documents, and creating ranked dataframes.

- `README.md`: This README file provides an overview of the project and usage instructions.

- `config.py`: Configuration file for specifying file paths and constants.

- `main.py`: The main Python script for running the candidate ranking system.

- `requirements.txt`: A file specifying Python package dependencies.


# Resume Matching and Ranking with DistilBERT

This project demonstrates how to match and rank resumes (CVs) with job descriptions using DistilBERT embeddings and cosine similarity. It includes utilities for PDF text extraction, text preprocessing, and ranking candidates based on similarity.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

## Prerequisites

- Python 3.x
- [PyTorch](https://pytorch.org/get-started/locally/) (for DistilBERT)
- [Transformers](https://huggingface.co/transformers/installation.html) library (for DistilBERT)
- Other required Python packages (install them using `pip`):

## Installation

Getting started with the Job Matching System is straightforward. Follow these installation steps:

1. Clone the repository:
 git clone https://github.com/yourusername/your-repo-name.git

2. Navigate to the project directory:
   cd your-repo-name

3. Install the required Python packages:
   pip install -r requirements.txt 

## Usage
1. Prepare your job descriptions in a CSV file (job_descriptions.csv) with a column named job_description.

2. Organize your candidate CVs in a folder (candidate_cvs) containing PDF files. The PDFs should include job role, skills, and education sections.

3. Update the paths and configuration in config.py according to your file structure.

4. Run the main script:
   python main.py

5. The script will calculate rankings, find and export top candidates, and print the top candidates for each job description.

## Customization
- You can adjust the DistilBERT model and tokenizer in distilBert_embeddings.py to fine-tune the embeddings based on your requirements.
- Modify the PDF text extraction and preprocessing functions in pdf_extract_utils.py and preprocessing_utils.py to suit your specific needs.

## Credits and Acknowledgments
We extend our gratitude to the following individuals, libraries, and tools that have been instrumental in the development of the Job Matching System:

- John Doe for their valuable feedback and suggestions.
- The Hugging Face Transformers library for its powerful pretrained models.
- The NLTK library for efficient text preprocessing.
