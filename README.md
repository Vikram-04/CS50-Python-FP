# Movie Review Manager

#### Video Demo: [Movie Review Manager](https://youtu.be/17-JZaNH31M)

#### Description:

A Python-based command-line application that allows you to write, view, and manage movie reviews. The application fetches movie details from the OMDb API and stores reviews in a JSONL (JSON Lines) format for easy persistence and retrieval.

## Features

- **Write Reviews**: Add detailed reviews for movies with ratings
- **View Reviews**: Display individual or all saved reviews
- **Delete Reviews**: Remove reviews from your collection
- **Movie Details**: Automatically fetch movie information (title, director) from OMDb API
- **Rating System**: Rate movies with four categories:
  - Perfection
  - Go for it
  - Timepass
  - Skip
- **Statistics**: View statistics about your reviews
- **Data Persistence**: Reviews are stored in JSONL format for easy access and manipulation

## Project Structure

```
├── project.py          # Main CLI application with menu system
├── classes.py          # Movie and Review class definitions
├── helpers.py          # Helper functions for API calls
├── requirements.txt    # Project dependencies
├── reviews.jsonl       # Stored reviews (auto-generated)
├── test_project.py     # Test suite
└── README.md           # This file
```

## Installation

### Prerequisites

- Python 3.6 or higher
- Internet connection (for OMDb API access)

### Setup

1. Clone or download the project files

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

The project requires:

- `requests` - For making HTTP requests to OMDb API
- `pytest` - For running tests

## Usage

### Running the Application

```bash
python project.py
```

This will display the main menu with the following options:

```
1. Write a review
2. View a review
3. View all reviews
4. Delete a review
5. Statistics
6. Exit
```

### Menu Options

**1. Write a review**

- Enter a movie name
- The application fetches the movie details from OMDb API
- Select a rating (Perfection, Go for it, Timepass, Skip)
- Write your review text
- Review is saved to `reviews.jsonl`

**2. View a review**

- Enter the movie name to view its review

**3. View all reviews**

- Displays all saved reviews in a formatted manner

**4. Delete a review**

- Enter the movie name to remove its review

**5. Statistics**

- View aggregate statistics about your reviews

**6. Exit**

- Quit the application

## Data Format

Reviews are stored in JSONL format (one JSON object per line):

```json
{
  "movie": { "name": "The Shawshank Redemption", "director": "Frank Darabont" },
  "rating": "Perfection",
  "text": "An absolute masterpiece of cinema"
}
```

## Testing

Run the test suite with pytest:

```bash
pytest test_project.py
```

## API Key

The application uses the OMDb API to fetch movie details. Consider:

- Getting your API key from [OMDb API](http://www.omdbapi.com/)
- Setting the API key as an environment variable

## Class Architecture

### Movie

- Stores movie name and director
- Validates non-empty movie names
- Can be converted to dictionary format

### Review

- Stores movie, rating, and review text
- Provides string representation for display
- Can be converted to/from dictionary format for JSON storage

## Error Handling

The application includes comprehensive error handling for:

- Invalid user input
- Network connectivity issues
- API errors
- File I/O operations
- Data validation errors

## Future Enhancements

Potential improvements could include:

- Web based interface
- Search and filter functionality
- Detailed statistics
- Database integration instead of JSONL

## License

This is an educational project created as a final project for CS50's Introduction to Programming with Python.
