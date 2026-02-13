from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Get embedding vector for a single text using SentenceTransformer
    """
    return model.encode([text])[0]

def cosine_sim(vec1, vec2):
    """
    Compute cosine similarity between two vectors
    """
    return cosine_similarity([vec1], [vec2])[0][0]
