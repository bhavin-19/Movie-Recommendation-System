# 🎬 Movie Recommendation System

This project is a simple content-based movie recommender built using the **Bag-of-Words** technique and deployed using **Streamlit** for an interactive web interface.

---

## 🚀 Features

- 📚 **Content-Based Filtering** using Bag-of-Words
- 🔍 Recommends similar movies based on plot overviews
- 🌐 **Deployed with Streamlit** — easy to use in-browser interface

---

## 🛠️ Tech Stack

- Python
- Scikit-learn (CountVectorizer)
- Pandas / NumPy
- Streamlit (for deployment)

---

## 💡 How It Works

1. Textual movie descriptions are vectorized using **Bag-of-Words**.
2. Movie similarity is computed using **cosine similarity**.
3. Given a movie title, the system returns the top-N similar movies.

---

## 📦 Setup

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
