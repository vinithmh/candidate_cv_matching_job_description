# pdf_extract_utils.py

from os.path import join
from fitz import open as fitz_open
from pandas import DataFrame
from os import walk

# Define the function to extract text content from a PDF file using PyMuPDF
def extract_text_from_pdf(pdf_file_path):
    """
    Extract text content from a PDF file using PyMuPDF.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content.
    """
    doc = fitz_open(pdf_file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

# Define the function to extract the job role from a PDF file
def extract_job_role_from_pdf(pdf_file_path):
    """
    Extract the job role from the first line of text in a PDF file.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: The extracted job role.
    """
    job_role = ""
    try:
        pdf_text = extract_text_from_pdf(pdf_file_path)
        job_role = pdf_text.split('\n')[0].strip()
    except Exception as e:
        print(f"Error extracting job role from {pdf_file_path}: {str(e)}")
    return job_role


# Define the function to extract the skills section from a PDF file's text content
def extract_skills_from_pdf(pdf_file_path):
    """
    Extract the skills section from a PDF file's text content.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: The extracted skills section.
    """
    skills = ""
    try:
        pdf_text = extract_text_from_pdf(pdf_file_path)

        # Extract the "Skills" section
        in_skills_section = False
        lines = pdf_text.split('\n')

        for line in lines:
            if "Skills" in line:
                in_skills_section = True
            elif in_skills_section and line.strip() == "":
                break  # Exit the skills section when encountering an empty line
            elif in_skills_section:
                skills += line + "\n"
    except Exception as e:
        print(f"Error extracting skills from {pdf_file_path}: {str(e)}")
    return skills


# Define the function to extract the education section from a PDF file's text content
def extract_education_from_pdf(pdf_file_path):
    """
    Extract the education section from a PDF file's text content.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: The extracted education section.
    """
    education = ""
    try:
        pdf_text = extract_text_from_pdf(pdf_file_path)

        # Extract the "Education" section
        in_education_section = False
        lines = pdf_text.split('\n')

        for line in lines:
            if "Education" in line:
                in_education_section = True
            elif in_education_section and line.strip() == "":
                break  # Exit the education section when encountering an empty line
            elif in_education_section:
                education += line + "\n"
    except Exception as e:
        print(f"Error extracting education from {pdf_file_path}: {str(e)}")
    return education


# Define the function to extract job details from a folder of PDFs and organize them into a corpus
def extract_and_clean_data(root_folder):
    """
    Extract job details from a folder of PDFs, organize them into a corpus,
    and create DataFrames with combined 'Job Role,' 'Skills,' and 'Education' columns.

    Args:
        root_folder (str): The path to the root folder containing PDF files.

    Returns:
        dict: A dictionary of DataFrames, each representing a subfolder's data.
    """
    corpus = {}

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith(".pdf"):
                pdf_path = join(dirpath, file)
                job_role = extract_job_role_from_pdf(pdf_path)
                skills = extract_skills_from_pdf(pdf_path)
                education = extract_education_from_pdf(pdf_path)

                # Remove "Skills" and "Education" labels
                skills = skills.replace("Skills", "").strip()
                education = education.replace("Education", "").strip()

                # Get the PDF file name
                pdf_file_name = os.path.basename(pdf_path)

                # Create a subfolder-based corpus
                subfolder = os.path.basename(dirpath)
                if subfolder not in corpus:
                    corpus[subfolder] = {"PDF File Name": [], "Job Role": [], "Skills": [], "Education": []}

                corpus[subfolder]["PDF File Name"].append(pdf_file_name)
                corpus[subfolder]["Job Role"].append(job_role)
                corpus[subfolder]["Skills"].append(skills)
                corpus[subfolder]["Education"].append(education)

    # Clean the extracted data and create DataFrames
    cleaned_corpus = {}
    for subfolder, details_dict in corpus.items():
        # Ensure all lists have the same length by padding with empty strings
        max_length = max(len(details_dict["Job Role"]), len(details_dict["Skills"]), len(details_dict["Education"]))
        details_dict["Job Role"] += [''] * (max_length - len(details_dict["Job Role"]))
        details_dict["Skills"] += [''] * (max_length - len(details_dict["Skills"]))
        details_dict["Education"] += [''] * (max_length - len(details_dict["Education"]))

        cleaned_corpus[subfolder] = details_dict

        # Create DataFrames
        df = DataFrame(details_dict)

        # Combine "Job Role," "Skills," and "Education" columns into a single column with spaces
        df["Details"] = df["Job Role"] + " " + df["Skills"] + " " + df["Education"]

        # Drop the individual columns
        df.drop(columns=["Job Role", "Skills", "Education"], inplace=True)

        cleaned_corpus[subfolder] = df

    return cleaned_corpus
