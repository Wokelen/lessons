#from dao.movie import MovieDAO
from my_lessons.HW_18_hard.hard.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_dir_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, mov_dict):
        return self.dao.create(mov_dict)

    def update(self, mov_dict):
        self.dao.update(mov_dict)
        return self.dao

    def delete(self, bid):
        self.dao.delete(bid)