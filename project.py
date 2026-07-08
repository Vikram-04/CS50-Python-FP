from classes import Movie, Review
from helpers import get_movie_details
import json
from pathlib import Path

OPTIONS = ["Write a review", "View a review", "View all reviews", "Delete a review", "Statistics", "Exit"]
RATINGS = ["Perfection", "Go for it", "Timepass", "Skip"]
FILE = Path("reviews.jsonl")


def display_menu(options):
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")


def get_choice(options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if not (1 <= choice <= len(options)):
                raise ValueError
            return choice
        except ValueError:
            print("Enter a valid choice")


def get_movie_name():
    while True:
        try:
            name = input("Movie name: ").strip()
            if not name:
                raise ValueError("Movie name cannot be empty")
            return name
        except ValueError as e:
            print(e)
            continue


def get_movie():
    try:
        name = get_movie_name()

        details = get_movie_details(name)
        if not details:
            raise ValueError("Movie details could not be found")
        return Movie(details)
    except (TypeError, ValueError, KeyError) as exc:
        print(exc)
        return None


def create_review(movie):
    if movie is None:
        print("No movie selected")
        return None

    try:
        display_menu(RATINGS)
        rating_choice = get_choice(RATINGS)
        text = input("Review: ").strip()
        if not text:
            raise ValueError("Review cannot be empty")
        return Review(movie, RATINGS[rating_choice - 1], text)
    except (ValueError, IndexError) as exc:
        print(exc)
        return None


def save_review(review, path=FILE):
    try:
        if review is None:
            raise ValueError("No review to save")

        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(review.to_dict()) + "\n")
        return True
    except (OSError, TypeError, ValueError) as exc:
        print(f"Could not save review: {exc}")
        return False


def save_reviews(reviews, path=FILE):
    try:
        with path.open("w", encoding="utf-8") as f:
            for review in reviews:
                f.write(json.dumps(review) + "\n")
        return True
    except (OSError, TypeError, ValueError) as exc:
        print(f"Could not save reviews: {exc}")
        return False


def read_jsonl(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    except Exception:
        return


def load_reviews(path=FILE):
    try:
        return list(read_jsonl(path))
    except TypeError:
        return []


def get_review(name, path=FILE):
    try:
        if not name:
            raise ValueError("Movie name cannot be empty")

        for review in load_reviews(path):
            if review["movie"]["name"].lower() == name.lower():
                return review
        return None
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        print(f"Could not find review: {exc}")
        return None


def view_all_reviews(path=FILE):
    try:
        reviews = load_reviews(path)
        if not reviews:
            print("No reviews yet")
            return []

        for review in reviews:
            print(Review.from_dict(review))
            
    except Exception as exc:
        print(f"Could not display reviews: {exc}")


def delete_review(name, path=FILE):
    try:
        reviews = load_reviews(path)
        if not reviews:
            print("No reviews found")
            return None

        updated_reviews = []
        removed_review = None

        for review in reviews:
            if review["movie"]["name"].lower() == name.lower():
                removed_review = review
            else:
                updated_reviews.append(review)

        if removed_review is None:
            print("Movie not reviewed")
            return None

        save_reviews(updated_reviews, path)
        return removed_review
    except (AttributeError, KeyError, TypeError, ValueError, OSError) as exc:
        print(f"Could not delete review: {exc}")
        return None


def get_statistics(path=FILE):
    try:
        reviews = load_reviews(path)
        director_counts = {}

        for review in reviews:
            director = review["movie"]["director"]
            director_counts[director] = director_counts.get(director, 0) + 1

        if director_counts:
            most_watched_director = max(director_counts, key=director_counts.get)
        else:
            most_watched_director = "None"

        return {
            "review_count": len(reviews),
            "most_watched_director": most_watched_director,
        }
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        print(f"Could not calculate statistics: {exc}")
        return {"review_count": 0, "most_watched_director": "None"}


def print_statistics(path=FILE):
    stats = get_statistics(path)
    print(f"Total reviews: {stats['review_count']}")
    print(f"Most watched director: {stats['most_watched_director']}")


def main():
    while True:
        display_menu(OPTIONS)
        choice = get_choice(OPTIONS)

        match(choice):
            case 1:
                movie = get_movie()
                review = create_review(movie)
                if review is not None:
                    save_review(review)
            case 2:
                review = get_review(get_movie_name())
                if review:
                    print(Review.from_dict(review))
                else:
                    print("Movie not reviewed")
            case 3:
                view_all_reviews()
            case 4:
                delete_review(get_movie_name())
            case 5:
                print_statistics()
            case 6:
                exit(0)

if __name__ == "__main__":
    main()