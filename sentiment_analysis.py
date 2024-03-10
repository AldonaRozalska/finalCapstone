import spacy
from textblob import TextBlob
import pandas as pd

# Read the CSV file containing Amazon product reviews
amazon_product_review = pd.read_csv('amazon_product_review.csv', low_memory=False)
# Sample 100 random reviews from the dataset
amazon_product_review = amazon_product_review.sample(100)
# Display the first few rows of the dataframe
amazon_product_review.head()

# Load the spaCy model for English language
nlp = spacy.load('en_core_web_sm')

# Function to preprocess text data
def preprocess_text(text):
    # Create a spaCy document from the input text
    doc = nlp(text)
    # Remove stopwords and non-alphabetic tokens, convert to lowercase and strip whitespace
    clean_tokens = [token.text.lower().strip() for token in doc if not token.is_stop and token.text.isalpha()]
    # Join the cleaned tokens back into a single string
    clean_text = ' '.join(clean_tokens)
    return clean_text

# Function for sentiment analysis using TextBlob
def analyze_sentiment(review_text):
    # Create a TextBlob object from the review text
    blob = TextBlob(review_text)
    # Retrieve the polarity score which indicates sentiment
    polarity = blob.sentiment.polarity
    # Determine sentiment as positive, negative, or neutral based on polarity score
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment, polarity

# Function to test sentiment analysis on product reviews
def test_sentiment_analysis(amazon_product_review):
    # Select the 'reviews.text' column and drop any missing values
    clean_data = amazon_product_review.dropna(subset=['reviews.text'])
    reviews_data = clean_data['reviews.text']

    # Analyze sentiment of the first 10 reviews and print the results
    for review in reviews_data.head(10):
        sentiment, polarity = analyze_sentiment(review)
        print(f"Review: {review}\nSentiment: {sentiment}, Polarity: {polarity}\n")

# Function to compare the similarity of two product reviews
def compare_review_similarity(amazon_product_review, index1, index2):
    # Check if the provided indices are within the dataframe's range
    if index1 >= len(amazon_product_review) or index2 >= len(amazon_product_review):
        raise IndexError("Index out of bounds")

    # Retrieve the reviews text using the provided indices
    review1 = amazon_product_review['reviews.text'].iloc[index1]
    review2 = amazon_product_review['reviews.text'].iloc[index2]

    # Create spaCy documents for both reviews
    doc1 = nlp(review1)
    doc2 = nlp(review2)

    # Calculate and print the similarity score between the two reviews
    similarity = doc1.similarity(doc2)
    print(f"Similarity between review {index1} and review {index2}: {similarity}")

# Main execution block
if __name__ == "__main__":
    # Test the sentiment analysis function on the sampled reviews
    test_sentiment_analysis(amazon_product_review)

    # Compare the similarity of the first two product reviews in the sample
    compare_review_similarity(amazon_product_review, 0, 1)