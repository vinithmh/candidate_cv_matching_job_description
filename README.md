# Job Matching System

![Project Logo](logo.png) <!-- Add your project logo or relevant image here -->

## Introduction

The Job Matching System is an advanced Python-based project that leverages state-of-the-art Natural Language Processing (NLP) techniques to streamline the process of matching job descriptions with candidate resumes. This project showcases a rich set of skills and capabilities that make it a valuable tool for HR professionals and hiring managers seeking efficient and effective candidate screening.

## Purpose

The primary purpose of the Job Matching System is to address the challenges faced during the hiring process, such as:

- Sorting through a large volume of resumes to identify suitable candidates.
- Ensuring that candidate qualifications align with job requirements.
- Minimizing human bias and errors in the candidate screening process.
- Saving time and resources by automating repetitive tasks.

By automating the matching process and providing a data-driven approach, this tool helps organizations identify the most qualified candidates quickly and effectively.

## Key Skills and Capabilities Demonstrated
### 1. Data Extraction from PDFs
   
One of the core functionalities of the Job Matching System is its ability to extract vital information from candidate resumes in PDF format. This is achieved using the PyMuPDF library (PyMuPDF is now known as fitz), and it showcases the following skills:

- **PDF Parsing**: The system demonstrates the ability to parse PDF documents efficiently, extracting text data for further analysis.

- **Error Handling**: Robust error handling ensures the project gracefully handles exceptions that may arise during the PDF extraction process.

### 2. Text Data Preprocessing

Before performing any analysis, the system preprocesses both job descriptions and candidate resumes. This step is crucial for ensuring data consistency and meaningful comparisons. Key skills demonstrated include:

- **Text Tokenization**: Utilizing the Hugging Face Transformers library, the system tokenizes text data, preparing it for subsequent analysis.

- **Lowercasing**: Text data is converted to lowercase, ensuring that case sensitivity does not affect similarity calculations.

- **Stopword Removal**: The project employs the NLTK library to remove stopwords from the text, eliminating common words that do not contribute significantly to the analysis.

- **Lemmatization**: The NLTK library is used again for lemmatizing words, reducing inflected words to their base form, improving analysis accuracy.

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

- **Utilization of Pretrained Models**: Leveraging state-of-the-art pretrained models like DistilBERT from Hugging Face, the system converts text data into dense vector representations (embeddings).

- **Calculation of Cosine Similarities**: The project calculates cosine similarities between job descriptions and candidate resumes to determine the best fit candidates for each position.

- **Dynamic Data Mapping**: The system dynamically maps job titles to corresponding candidate resume datasets, allowing for flexibility and scalability across industries and job roles.

## Getting Started
To get started with the Job Matching System, follow these steps:

- Clone the repository to your local machine.
- Install the required Python libraries using pip install -r requirements.txt.
- Organize your candidate resumes in PDF format within subdirectories (each subdirectory representing a job position).
- Run the provided Python scripts to extract, preprocess, and match job descriptions with candidate resumes.

## Installation

Getting started with the Job Matching System is straightforward. Follow these installation steps:

1. **Clone the Repository**: Clone the project repository to your local machine using Git.
   ```shell
   git clone https://github.com/yourusername/JobMatchingSystem.git
