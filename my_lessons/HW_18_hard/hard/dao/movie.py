from dao.model.movie import Movie


class MovieDAO():
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_dir_id(self,val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self,val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self,val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, mov_dict):
        data = Movie(**mov_dict)
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self,bid):
        movie = self.get_one(bid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, mov_dict):
        movie = self.get_one(mov_dict.get("id"))
        movie.title = mov_dict.get("title")
        movie.description = mov_dict.get("description")
        movie.trailer = mov_dict.get("trailer")
        movie.year = mov_dict.get("year")
        movie.raiting = mov_dict.get("raiting")
        movie.genre_id = mov_dict.get("genre_id")
        movie.director_id = mov_dict.get("director_id")
        self.session.add(movie)
        self.session.commit()
