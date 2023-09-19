# distilBert_embeddings.py

from torch.autograd import no_grad
from transformers import DistilBertTokenizer, DistilBertModel

# Initialize DistilBERT model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

# Function to extract DistilBERT embeddings
def extract_distilbert_embeddings(text):
    """
    Extract DistilBERT embeddings from text.

    Args:
        text (str): The input text from which embeddings should be extracted.

    Returns:
        list: List of DistilBERT embeddings for the text.
    """
    # Tokenize text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)

    # Generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract embeddings for the [CLS] token (you can adjust this depending on your needs)
    cls_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

    return cls_embedding

