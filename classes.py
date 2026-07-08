class Movie:
    def __init__(self, details):
        self.name = details["Title"]
        self.director = details["Director"]
    
    def __str__(self):
        return f"Movie: {self.name}, Director: {self.director}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: raise ValueError("Enter a non-empty name")
        self._name = name

    def to_dict(self):
        return {"name": self.name, "director": self.director}

class Review:
    def __init__(self, movie, rating, text):
        self.movie = movie
        self.rating = rating
        self.text = text 
    def  __str__(self):
        print()
        return f"---------------------------------------------------\n{self.movie.name}\nRating: {self.rating}\nReview: {self.text}\n---------------------------------------------------"
    
    def to_dict(self):
        return {"movie": self.movie.to_dict(), "rating": self.rating, "text":self.text}
    
    @classmethod   
    def from_dict(cls, d):
        movie = {'Title': d['movie']['name'], 'Director': d['movie']['director']}
        return cls(Movie(movie), d['rating'], d['text'])