"""
CODSOFT - Artificial Intelligence Internship
Task 3: Movie Recommendation System

Uses Content-Based Filtering with TF-IDF and Cosine Similarity
to recommend movies based on genre, description and ratings.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── Dataset ────────────────────────────────────────────────────────────────
movies = pd.DataFrame({
    "title": [
        "The Dark Knight", "Inception", "Interstellar", "The Matrix",
        "Avengers Endgame", "Iron Man", "Doctor Strange", "Thor Ragnarok",
        "The Godfather", "Goodfellas", "Scarface", "The Departed",
        "Titanic", "The Notebook", "Pride and Prejudice", "La La Land",
        "The Shining", "Get Out", "A Quiet Place", "It",
        "Toy Story", "Finding Nemo", "The Lion King", "Frozen",
        "Forrest Gump", "The Pursuit of Happyness", "A Beautiful Mind", "Cast Away"
    ],
    "genre": [
        "Action Crime Thriller", "Action Sci-Fi Thriller", "Sci-Fi Drama Adventure", "Sci-Fi Action",
        "Action Adventure Superhero", "Action Adventure Superhero", "Action Adventure Superhero", "Action Comedy Superhero",
        "Crime Drama", "Crime Drama", "Crime Drama", "Crime Thriller Drama",
        "Romance Drama", "Romance Drama", "Romance Drama", "Romance Musical Drama",
        "Horror Thriller", "Horror Thriller", "Horror Sci-Fi", "Horror",
        "Animation Comedy Adventure", "Animation Comedy Adventure", "Animation Drama Adventure", "Animation Musical Adventure",
        "Drama Comedy Romance", "Drama Biography", "Drama Biography", "Drama Adventure"
    ],
    "description": [
        "Batman fights the Joker who wants to plunge Gotham into anarchy",
        "A thief who steals secrets through dreams takes a job to plant an idea",
        "Astronauts travel through a wormhole in search of a new home for humanity",
        "A hacker discovers reality is a simulation and joins a rebellion",
        "Avengers assemble to reverse Thanos devastating snap and save the universe",
        "Billionaire Tony Stark builds a powered armor suit and becomes Iron Man",
        "A surgeon becomes a sorcerer supreme to protect earth from mystical threats",
        "Thor teams with the Hulk to stop his sister from destroying Asgard",
        "The aging patriarch of an organized crime dynasty transfers control to his son",
        "The story of Henry Hill and his life in the mob covering his rise and fall",
        "A Cuban immigrant becomes a powerful drug lord in Miami",
        "An undercover cop and a mole in the police try to identify each other",
        "A poor artist falls in love with a socialite aboard the ill-fated Titanic",
        "A couple falls in love but are separated by their families and time",
        "Two sisters of vastly different temperaments fall in love against social norms",
        "A jazz pianist and an aspiring actress fall in love while pursuing their dreams",
        "A family struggles to survive in an isolated hotel haunted by dark forces",
        "A young African American discovers his girlfriend family has a disturbing secret",
        "A family on a farm must live in silence while hiding from creatures that hunt by sound",
        "A group of kids in a small town fight a shapeshifting monster called Pennywise",
        "A cowboy doll feels threatened when a new space toy becomes the owner favorite",
        "A clownfish searches the ocean to find his missing son",
        "A young lion prince flees his kingdom after the murder of his father",
        "A princess with magical icy powers goes on a journey with her sister",
        "A simple man with low IQ witnesses and influences historical events in America",
        "A homeless father in San Francisco pursues happiness and a career as a stockbroker",
        "A brilliant mathematician struggles with schizophrenia while making important discoveries",
        "A man stranded on an island for years struggles to survive and return home"
    ],
    "rating": [
        9.0, 8.8, 8.6, 8.7,
        8.4, 7.9, 7.5, 7.9,
        9.2, 8.7, 8.3, 8.5,
        7.8, 7.9, 7.8, 8.0,
        8.4, 7.7, 7.5, 7.3,
        8.3, 8.1, 8.5, 7.4,
        8.8, 8.0, 8.2, 7.8
    ]
})

# ── Content-Based Filtering ────────────────────────────────────────────────

# Combine genre + description into one text feature
movies["features"] = movies["genre"] + " " + movies["description"]

# TF-IDF Vectorizer converts text to numerical vectors
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["features"])

# Cosine Similarity measures how similar two movies are
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend(movie_title, num_recommendations=5):
    movie_title = movie_title.strip().lower()
    titles_lower = movies["title"].str.lower().tolist()

    if movie_title not in titles_lower:
        print(f"\n Sorry! '{movie_title}' not found in our database.")
        print(" Available movies:")
        for i, t in enumerate(movies["title"].tolist(), 1):
            print(f"  {i}. {t}")
        return

    idx = titles_lower.index(movie_title)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [s for s in sim_scores if s[0] != idx][:num_recommendations]

    print(f"\n🎬 Because you liked '{movies['title'][idx]}', we recommend:\n")
    print(f"  {'#':<4} {'Title':<30} {'Genre':<30} {'Rating'}")
    print("  " + "-" * 75)
    for i, (movie_idx, score) in enumerate(sim_scores, 1):
        title  = movies["title"][movie_idx]
        genre  = movies["genre"][movie_idx].split()[0]
        rating = movies["rating"][movie_idx]
        print(f"  {i:<4} {title:<30} {genre:<30} ⭐ {rating}")


def show_all_movies():
    print("\n📽️  Available Movies:\n")
    for i, row in movies.iterrows():
        print(f"  {i+1:>2}. {row['title']:<30} ⭐ {row['rating']}")


# ── Main Loop ──────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("   🎬  Movie Recommendation System  |  CodSoft")
    print("=" * 55)
    print("  Using: Content-Based Filtering + Cosine Similarity")
    print("=" * 55)

    while True:
        print("\n  Options:")
        print("  1. Get movie recommendations")
        print("  2. Show all movies")
        print("  3. Exit")

        choice = input("\n  Enter choice (1/2/3): ").strip()

        if choice == "1":
            movie = input("\n  Enter a movie name: ")
            recommend(movie)
        elif choice == "2":
            show_all_movies()
        elif choice == "3":
            print("\n  Goodbye! Happy Watching 🎥\n")
            break
        else:
            print("  Invalid choice! Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
