## [Movie Suggestions](https://www.google.com/maps/search/https%3A%2F%2Fgithub.com%2Fankit4101%2Fmovie-suggestions)

---

# 🎬 Movie Suggestions

A simple yet effective movie recommendation system that suggests 5 movies similar to the one you enter. Built using the TMDb 5000 Movie Dataset and powered by natural language processing techniques.

---

## 📊 Dataset

This project utilizes the [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which contains metadata for 5,000 movies, including overviews, genres, cast, crew, and more. 

---

## 🧠 How It Works

1. **Data Preprocessing**: Movie overviews are cleaned and stemmed to reduce words to their root forms.
2. **Feature Extraction**: Utilizes Count Vectorization to convert text data into numerical feature vectors.
3. **Similarity Computation**: Calculates cosine similarity between movie vectors to determine similarity scores.
4. **Recommendation**: For a given movie, the system retrieves the top 5 most similar movies based on the similarity scores.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x

* Install the required packages:

```bash
  pip install -r requirements.txt
```



### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/ankit4101/movie-suggestions.git
   cd movie-suggestions
   ```



2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```



3. Open your browser and navigate to `http://localhost:8501` to use the application.

---

## 🖥️ Live Demo

Experience the application live: [movies-suggestions.streamlit.app](https://movies-suggestions.streamlit.app)

---

## 📁 Project Structure

```plaintext
movie-suggestions/
├── app.py
├── movie-recommender-system.ipynb
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
└── readme.md
```



* `app.py`: Main application file for the Streamlit interface.
* `movie-recommender-system.ipynb`: Jupyter notebook containing the data preprocessing and model building steps.
* `movie_dict.pkl`: Serialized dictionary containing movie data.
* `similarity.pkl`: Serialized similarity matrix used for recommendations.
* `requirements.txt`: List of Python dependencies.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any inquiries or feedback, please contact [Ankit](https://github.com/ankit4101).

---

*Note: This project is for educational purposes and is not affiliated with TMDb.*

---
