# Task 3 - Movie Recommendation System

A content-based movie recommendation system built for the CodSoft Artificial Intelligence Internship.
It recommends movies based on genre and description similarity using **TF-IDF** and **Cosine Similarity**.

## How to run

### Install required libraries first:
```bash
pip install pandas scikit-learn
```

### Then run:
```bash
python movie_recommender.py
```

## How it works
1. Enter a movie name you like
2. System finds similar movies based on genre + description
3. Top 5 recommendations are shown with ratings

## Algorithm: Content-Based Filtering
- **TF-IDF Vectorizer** converts movie genres and descriptions into numerical vectors
- **Cosine Similarity** measures how similar two movies are to each other
- Movies with highest similarity scores are recommended

## Example
```
Enter a movie name: The Dark Knight

Because you liked 'The Dark Knight', we recommend:
  1   The Departed        Crime    ⭐ 8.5
  2   The Godfather       Crime    ⭐ 9.2
  3   Inception           Action   ⭐ 8.8
  4   Scarface            Crime    ⭐ 8.3
  5   The Shining         Horror   ⭐ 8.4
```

## Movies included (28 movies across 7 genres)
- Action / Superhero
- Crime / Thriller
- Sci-Fi
- Romance / Drama
- Horror
- Animation
- Biography

---
Built as part of the **#codsoft** Artificial Intelligence Internship.
