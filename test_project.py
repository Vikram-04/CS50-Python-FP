from project import save_review, load_reviews, get_review, delete_review, get_statistics
from classes import Movie, Review
from pathlib import Path

path = Path("test_reviews.jsonl")
path.write_text("")
movie = Movie({
        "Title": "Interstellar",
        "Director": "Christopher Nolan"
    })
review = Review(movie, "Perfection", "Amazing movie")


def test_save_review():
    assert save_review(review, path) == True

def test_load_reviews():
    reviews = load_reviews(path)
    assert len(reviews) == 1
    assert reviews[0]["movie"]["name"] == "Interstellar"
    assert reviews[0]["rating"] == "Perfection"


def test_get_review():
    found = get_review("Interstellar", path)
    assert found["movie"]["name"] == "Interstellar"


def test_delete_review():
    deleted = delete_review("Interstellar", path)
    assert deleted["movie"]["name"] == "Interstellar"
    assert load_reviews(path) == []
    assert delete_review("Enola holmes", path) is None


def test_get_statistics():
    stats = get_statistics(path)
    assert stats["review_count"] == 0
    assert stats["most_watched_director"] == "None"
    save_review(review, path)
    stats = get_statistics(path)
    assert stats["review_count"] == 1
    assert stats["most_watched_director"] == "Christopher Nolan"