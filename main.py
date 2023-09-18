import pandas as pd
from config import JOB_DESCRIPTIONS_FILE, DATAFRAMES_DIR, JOB_DESCRIPTION_COLUMN
from utils.pdf_extract_utils import extract_and_clean_data
from utils.preprocessing_utils import preprocess_text
from utils.distilBert_embbedings import extract_distilbert_embeddings
from utils.ranking_utils import calculate_rankings, export_rankings, find_top_candidates, export_top_candidates, print_top_candidates, print_rankings

def main():
    # Load job descriptions and dataframes
    sel_job_desp_df = pd.read_csv(JOB_DESCRIPTIONS_FILE)
    dataframes = extract_and_clean_data(DATAFRAMES_DIR)

    # Apply the preprocess_text function to the "job_description" column
    sel_job_desp_df[JOB_DESCRIPTION_COLUMN] = sel_job_desp_df[JOB_DESCRIPTION_COLUMN].apply(preprocess_text)

    # Iterate through the dataframes dictionary and apply preprocessing to the "Details" column
    for subfolder, df in dataframes.items():
        # Apply the preprocess_text function to the "Details" column
        df["Details"] = df["Details"].apply(preprocess_text)

    # Apply DistilBERT embedding extraction to 'job_description' column in sel_job_desp_df
    sel_job_desp_df[JOB_DESCRIPTION_COLUMN] = sel_job_desp_df[JOB_DESCRIPTION_COLUMN].apply(extract_distilbert_embeddings)

    # Iterate through the dataframes dictionary and apply DistilBERT embedding extraction to 'Details' column
    for subfolder, df in dataframes.items():
        df['Details'] = df['Details'].apply(extract_distilbert_embeddings)

    # Calculate rankings
    dataframes_with_ranks = calculate_rankings(sel_job_desp_df, dataframes)

    # Export rankings
    export_rankings(dataframes_with_ranks)

    # Find and export top candidates
    top_5_cvs = find_top_candidates(dataframes, sel_job_desp_df)
    export_top_candidates(top_5_cvs)

    # Print rankings of all the candidates
    print_rankings(dataframes_with_ranks)

    # Print top candidates
    print_top_candidates(top_5_cvs)

if __name__ == "__main__":
    main()
