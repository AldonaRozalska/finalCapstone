# Amazon Product Review Sentiment Analysis

## Description

This capstone project is designed to analyze sentiments expressed in Amazon product reviews. It utilizes the spaCy library for natural language processing to preprocess the text data and the TextBlob library to determine the sentiment polarity of each review. The project aims to classify the reviews into positive, negative, or neutral categories and also includes functionality to compare the similarity between two reviews using spaCy's similarity features.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

Before running the sentiment analysis, ensure you have Python installed on your system along with the following libraries: `spacy`, `textblob`, and `pandas`.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/AldonaRozalska/finalCapstone.git

2. Navigate to the project directory:
   ```bash
   cd finalCapstone

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
4. Download the necessary spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm

## Usage
To perform sentiment analysis on your dataset, follow these steps:

Ensure that the dataset file amazon_product_review.csv is placed in the project directory.
Run the sentiment analysis script:
   ```bash
   python sentiment_analysis.py

Example Output:

   # Example output from sentiment analysis
   Review: This product is amazing!
   Sentiment: positive, Polarity: 0.6

   # Example output from similarity comparison
   Similarity between review 0 and review 1: 0.85

```
## Credits

This project was created by [Aldona Rozalska](https://github.com/AldonaRozalska) as part of a capstone project.



