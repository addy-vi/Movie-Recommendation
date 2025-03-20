# Movie Recommendation System Using Cosine Similarity and Difflib

## Introduction
This project implements a **Movie Recommendation System** using **Cosine Similarity** and the **difflib** library to recommend movies based on user input. Cosine Similarity is a measure of similarity between two non-zero vectors in an inner product space, which in this case, is used to calculate the similarity between movie titles. **difflib** is used to match user input with movie titles in the dataset. This approach allows users to find the most similar movies based on a movie title or genre.

## Objectives
- Build a recommendation system to suggest similar movies based on a given movie title.
- Use **Cosine Similarity** to measure similarity between movie titles.
- Use **difflib** to match user input to movie titles from the dataset.
- Provide a list of recommended movies with high similarity to the given movie.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: pandas, numpy, sklearn, difflib
- **Tools**: Jupyter Notebook, VS Code
- **Dataset**: MovieLens dataset or any other dataset containing movie titles and genres.

## Dataset Information
This project uses the **MovieLens** dataset (or any other dataset containing movie details such as title, genres, etc.). The dataset consists of the following columns:
- **movieId**: Unique identifier for each movie.
- **title**: The title of the movie.
- **genres**: Genre(s) of the movie (e.g., Action, Comedy, Drama, etc.).

You can use a dataset like [MovieLens Dataset](https://grouplens.org/datasets/movielens/) for testing.

## Workflow

### 1. **Data Collection:**
   - Download a movie dataset (e.g., MovieLens dataset).
   - Load the dataset into a pandas DataFrame.

### 2. **Data Preprocessing:**
   - Clean and preprocess the dataset to remove duplicates and handle missing values.
   - Extract relevant columns (movieId, title, genres) from the dataset for the recommendation system.

### 3. **Building the Recommendation System:**
   - Use **Cosine Similarity** to measure the similarity between movie titles.
   - Use **difflib** to match user input to movie titles from the dataset.
   - Retrieve a list of movies with high similarity scores and recommend them to the user.

### 4. **Making Predictions:**
   - Given a movie title, the system will suggest the most similar movies based on the cosine similarity score.

### 5. **Results:**
   - Display a list of recommended movies along with similarity scores.

## Results
- **Recommendation output**: The system will recommend a list of similar movies based on cosine similarity scores.
- **Expected accuracy**: The recommendations should be relevant based on the similarity of movie titles and genres.

## Future Work
- Integrate additional data such as movie ratings, user preferences, or reviews to improve recommendation accuracy.
- Use collaborative filtering techniques or neural networks for more advanced recommendation models.
- Deploy the recommendation system as a web application using frameworks like Flask or Django.

## Conclusion
This project demonstrates how to build a simple movie recommendation system using **Cosine Similarity** and **difflib**. The system matches user input with movie titles and provides recommendations based on similarity. It offers a foundation for more advanced recommendation algorithms and can be extended for real-world applications.

## Clone Repository

To clone this repository to your local machine, run the following command:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
