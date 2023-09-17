# Job Matching System

![Project Logo](logo.png) <!-- Add your project logo or relevant image here -->

## Introduction

The **Job Matching System** is an innovative and efficient solution for HR professionals and hiring managers seeking to simplify and optimize the candidate screening process. This Python-based tool leverages advanced Natural Language Processing (NLP) techniques, pretrained models, and data analysis to automate and improve the matching of job descriptions with candidate resumes.

### Purpose

The primary purpose of the Job Matching System is to address the challenges faced during the hiring process, such as:

- Sorting through a large volume of resumes to identify suitable candidates.
- Ensuring that candidate qualifications align with job requirements.
- Minimizing human bias and errors in the candidate screening process.
- Saving time and resources by automating repetitive tasks.

By automating the matching process and providing a data-driven approach, this tool helps organizations identify the most qualified candidates quickly and effectively.

## Features

The Job Matching System offers a range of features designed to streamline the hiring process:

- **Data Extraction from PDF Resumes**: The system can extract essential information from candidate resumes in PDF format, including job roles, skills, and education details.

- **Text Preprocessing for Consistency**: It preprocesses both job descriptions and resumes, ensuring consistency and meaningful comparisons by removing noise, stopwords, and inflections.

- **Utilization of Pretrained Models**: Leveraging state-of-the-art pretrained models like DistilBERT from Hugging Face, the system converts text data into dense vector representations (embeddings).

- **Calculation of Cosine Similarities**: The project calculates cosine similarities between job descriptions and candidate resumes to determine the best fit candidates for each position.

- **Dynamic Data Mapping**: The system dynamically maps job titles to corresponding candidate resume datasets, allowing for flexibility and scalability across industries and job roles.

## Installation

Getting started with the Job Matching System is straightforward. Follow these installation steps:

1. **Clone the Repository**: Clone the project repository to your local machine using Git.
   ```shell
   git clone https://github.com/yourusername/JobMatchingSystem.git
