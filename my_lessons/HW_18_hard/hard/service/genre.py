#from dao.genre import GenreDAO
from my_lessons.HW_18_hard.hard.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, gen_dict):
        return self.dao.create(gen_dict)

    def update(self, gen_dict):
        self.dao.update(gen_dict)
        return self.dao

    def delete(self, bid):
        self.dao.delete(bid)