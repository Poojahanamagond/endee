from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample resumes
resumes = [
    "Java developer with Spring Boot and MySQL experience",
    "Frontend developer with React and JavaScript skills",
    "Python developer with AI and Machine Learning knowledge"
]

# Convert resumes to embeddings
resume_embeddings = model.encode(resumes)

# Search query
query = input("Enter your search: ")

query_embedding = model.encode([query])

# Compare similarity
scores = np.dot(resume_embeddings, query_embedding.T)

# Get best match
best_match = np.argmax(scores)

print("\nBest Match Resume:")
print(resumes[best_match])