# ranking_utils.py

from sklearn.metrics.pairwise import cosine_similarity
from numpy import array, argsort
from pandas import DataFrame

def calculate_rankings(sel_job_desp_df, dataframes):
    position_title_mapping = dict(zip(sel_job_desp_df['position_title'], dataframes.keys()))
    dataframes_with_ranks = {}

    for position_title, job_description in zip(sel_job_desp_df['position_title'], sel_job_desp_df['job_description']):
        similarities = {}
        job_description = array(job_description).reshape(1, -1)  # Ensure job_description is a 2D array
        cv_df = dataframes[position_title_mapping[position_title]]  # Get the corresponding DataFrame
        cv_embeddings = array(list(cv_df['Details']))  # Assuming 'Details' column contains CV embeddings

        # Calculate cosine similarities within the corresponding DataFrame
        similarities = cosine_similarity(job_description, cv_embeddings)

        # Get the PDF file names and ranks based on similarity
        pdf_file_names = cv_df['PDF File Name']
        ranked_pdf_file_names = [pdf_file_names[i] for i in argsort(similarities[0])[::-1]]

        # Create a new DataFrame with PDF ranks and cosine similarities
        rank_df = DataFrame({'PDF File Name': ranked_pdf_file_names,
                             'Cosine Similarity': similarities[0][argsort(similarities[0])[::-1]]})

        # Store the dataframe in the dictionary
        dataframes_with_ranks[position_title] = rank_df

    return dataframes_with_ranks

def export_rankings(dataframes_with_ranks):
    for position_title, rank_df in dataframes_with_ranks.items():
        # Export the dataframe to a CSV file
        rank_df.to_csv(f'{position_title}_ranked.csv', index=False)

def find_top_candidates(dataframes, sel_job_desp_df):
    position_title_mapping = dict(zip(sel_job_desp_df['position_title'], dataframes.keys()))
    top_5_cvs = {}

    for position_title, job_description in zip(sel_job_desp_df['position_title'], sel_job_desp_df['job_description']):
        similarities = {}
        job_description = np.array(job_description).reshape(1, -1)  # Ensure job_description is a 2D array
        cv_df = dataframes[position_title_mapping[position_title]]  # Get the corresponding DataFrame
        cv_embeddings = np.array(list(cv_df['Details']))  # Assuming 'Details' column contains CV embeddings

        # Calculate cosine similarities within the corresponding DataFrame
        similarities = cosine_similarity(job_description, cv_embeddings)

        # Get the PDF file names and ranks based on similarity
        pdf_file_names = cv_df['PDF File Name']
        ranked_pdf_file_names = [(pdf_file_names[i], similarities[0][i]) for i in np.argsort(similarities[0])[-1:-6:-1]]

        # Store the ranked PDF file names along with similarity
        top_5_cvs[position_title] = ranked_pdf_file_names

    return top_5_cvs

def export_top_candidates(top_5_cvs):
    results_df = DataFrame.from_dict(top_5_cvs, orient='index', columns=['Rank 1 PDF File', 'Rank 2 PDF File', 'Rank 3 PDF File', 'Rank 4 PDF File', 'Rank 5 PDF File'])
    results_df.to_csv('top_5_cvs.csv')

def print_top_candidates(top_5_cvs):
    for position_title, top_pdf_similarities in top_5_cvs.items():
        print(f"Top 5 PDF Files for {position_title}:")
        for rank, (pdf_file, similarity) in enumerate(top_pdf_similarities, start=1):
            print(f"Rank {rank}: PDF File: {pdf_file}, Similarity: {similarity:.4f}")
        print("\n")

def print_rankings(dataframes_with_ranks):
    for position_title, rank_df in dataframes_with_ranks.items():
        print(f"Rankings for {position_title}:")
        for rank, (pdf_file, similarity) in enumerate(zip(rank_df['PDF File Name'], rank_df['Cosine Similarity']), start=1):
            print(f"Rank {rank}: PDF File: {pdf_file}, Cosine Similarity: {similarity:.4f}")
        print("\n")
